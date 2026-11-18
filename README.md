# Phishing Detection AI

A local web interface for trying the repository's trained email phishing classifier. The Flask app loads `model_phishing.pkl`, accepts an email subject and body, and displays the model's classification, phishing probability, and URL measurements from the existing feature extractor.

The URL measurements describe features found in the email. They are not explanations of why the Random Forest chose a particular label. This project is a coursework demonstration; its real-world detection performance has not been independently validated.

## Run the app

Use Python 3.10 or newer. From this folder in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Open `http://127.0.0.1:5000` in a browser. The trained model file must remain in the project root. The first analysis loads the model into memory; later analyses reuse it.

## API

`POST /api/analyze` accepts JSON with `subject` and `body` string fields. It returns `label` (`aman` or `phishing`), the numeric prediction, phishing probability, extracted URLs, and the URL measurements. `GET /api/health` reports whether the model artifact is present.

## Train the model again

The repository contains `data_siap_latih.csv`, which can be used directly by `2_train_model.py`. Run `.\.venv\Scripts\python.exe 2_train_model.py` to train and overwrite `model_phishing.pkl`.

To rebuild the prepared CSV, first place the CEAS_08 dataset at `CEAS_08.csv/CEAS_08.csv`, then run `.\.venv\Scripts\python.exe 1_persiapan_data.py`. The raw dataset is not included in this repository.

## Project files

- `app.py` — Flask web app and prediction API.
- `templates/` and `static/` — web interface.
- `feature_extractor.py` — text cleanup and URL feature extraction used by the model.
- `2_train_model.py` — pipeline training and evaluation.
- `model_phishing.pkl` — checked-in trained model pipeline.
- `data_siap_latih.csv` — prepared training data.
