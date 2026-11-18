import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from feature_extractor import UrlFeatureExtractor

print("Membaca data_siap_latih.csv...")
df = pd.read_csv('data_siap_latih.csv').dropna()

X = df[['teks_bersih']]
y = df['label_angka']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

preprocessor = ColumnTransformer(
    transformers=[
        ('teks', TfidfVectorizer(max_features=3000), 'teks_bersih'),
        ('url', UrlFeatureExtractor(), 'teks_bersih')
    ]
)

model_pipeline = Pipeline([
    ('fitur', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1))
])

print("Sedang melatih model AI (tunggu sekitar 1-3 menit)...")
model_pipeline.fit(X_train, y_train)

print("\n=== HASIL EVALUASI MODEL ===")
y_pred = model_pipeline.predict(X_test)

print("\n[1] Classification Report (Precision, Recall, F1):")
print(classification_report(y_test, y_pred, target_names=['Aman (0)', 'Phishing (1)']))

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

print("[2] Analisis Kesalahan (Confusion Matrix):")
print(f"- True Negative  (Aman ditebak Aman)              : {tn}")
print(f"- False Positive (Aman dituduh Phishing)         : {fp}")
print(f"- False Negative (Phishing lolos dianggap Aman)  : {fn}")
print(f"- True Positive  (Phishing ditangkap Phishing)   : {tp}")

joblib.dump(model_pipeline, 'model_phishing.pkl')
print("\nBerhasil! Model disimpan sebagai 'model_phishing.pkl'.")