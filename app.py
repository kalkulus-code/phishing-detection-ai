"""Small Flask API and web entry point for the trained phishing email model."""

from __future__ import annotations

import re
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request

from feature_extractor import UrlFeatureExtractor, bersihkan_teks


ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "model_phishing.pkl"
URL_PATTERN = re.compile(r'(https?://[^\s<>"\']+|www\.[^\s<>"\']+)', re.IGNORECASE)
MAX_EMAIL_LENGTH = 50_000

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 256 * 1024

_model = None


def get_model():
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(f"Model tidak ditemukan: {MODEL_PATH.name}")
        _model = joblib.load(MODEL_PATH)
    return _model


def inspect_urls(text: str) -> tuple[list[str], list[dict[str, object]]]:
    """Return URLs and observable URL traits; these are signals, not explanations."""
    urls = URL_PATTERN.findall(text)
    # The training pipeline extracts URL traits from the normalized text column.
    traits = UrlFeatureExtractor().transform([bersihkan_teks(text)])[0].tolist()
    names = [
        "Ada URL",
        "Jumlah URL",
        "Panjang URL pertama",
        "Jumlah titik pada URL pertama",
        "Jumlah tanda hubung pada URL pertama",
        "Memuat simbol @",
        "Menggunakan HTTPS",
        "Memuat alamat IP",
    ]
    values: list[object] = [
        bool(traits[0]),
        int(traits[1]),
        int(traits[2]),
        int(traits[3]),
        int(traits[4]),
        bool(traits[5]),
        bool(traits[6]),
        bool(traits[7]),
    ]
    return urls, [
        {"name": name, "value": value} for name, value in zip(names, values)
    ]


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/health")
def health():
    return jsonify({"ready": MODEL_PATH.exists(), "model": MODEL_PATH.name})


@app.post("/api/analyze")
def analyze():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Kirim data email dalam format JSON."}), 400

    subject = payload.get("subject", "")
    body = payload.get("body", "")
    if not isinstance(subject, str) or not isinstance(body, str):
        return jsonify({"error": "Subjek dan isi email harus berupa teks."}), 400
    if len(subject) + len(body) > MAX_EMAIL_LENGTH:
        return jsonify({"error": "Email terlalu panjang. Batasnya 50.000 karakter."}), 413

    combined = f"{subject} {body}".strip()
    if not combined:
        return jsonify({"error": "Tambahkan subjek atau isi email untuk dianalisis."}), 400

    clean_text = bersihkan_teks(combined)
    features = pd.DataFrame({"teks_bersih": [clean_text]})

    try:
        model = get_model()
        prediction = int(model.predict(features)[0])
        probability = model.predict_proba(features)[0]
        class_positions = {int(label): index for index, label in enumerate(model.classes_)}
        phishing_probability = float(probability[class_positions[1]])
    except Exception:
        app.logger.exception("Model gagal memproses email")
        return jsonify({"error": "Model belum siap digunakan. Periksa model_phishing.pkl dan dependensi Python."}), 503

    urls, url_signals = inspect_urls(combined)
    return jsonify(
        {
            "label": "phishing" if prediction == 1 else "aman",
            "prediction": prediction,
            "phishing_probability": phishing_probability,
            "url_count": len(urls),
            "urls": urls,
            "url_signals": url_signals,
        }
    )


@app.errorhandler(413)
def request_too_large(_error):
    return jsonify({"error": "Data terlalu besar untuk dianalisis."}), 413


if __name__ == "__main__":
    app.run(debug=False)
