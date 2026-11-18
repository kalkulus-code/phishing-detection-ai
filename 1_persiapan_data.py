import pandas as pd
from feature_extractor import UrlFeatureExtractor, bersihkan_teks

# 1. Sesuaikan path sesuai struktur folder di VS Code kamu
file_path = 'CEAS_08.csv/CEAS_08.csv' 

print("Membaca dataset...")
df = pd.read_csv(file_path)

# Hapus baris yang kosong pada kolom body atau label
df = df.dropna(subset=['body', 'label'])

# Gabungkan subject dan body agar analisis lebih akurat
df['teks_gabungan'] = df['subject'].fillna('') + " " + df['body'].fillna('')

# Label di CEAS_08 sudah berupa angka (1 = Phishing, 0 = Aman)
df['label_angka'] = df['label'].astype(int)

# Bersihkan teks email
df['teks_bersih'] = df['teks_gabungan'].apply(bersihkan_teks)

# Simpan dataset yang sudah bersih untuk dipakai Safid
df[['teks_bersih', 'label_angka']].to_csv('data_siap_latih.csv', index=False)
print(f"Berhasil! Total data bersih: {len(df)} baris.")
print(f"Jumlah Phishing (1): {sum(df['label_angka'] == 1)}")
print(f"Jumlah Aman (0)    : {sum(df['label_angka'] == 0)}")

# 2. Uji Coba Ekstraksi Fitur URL pada 3 sampel data
print("\n--- Menguji Ekstraksi Fitur URL ---")
extractor = UrlFeatureExtractor()
hasil_fitur = extractor.transform(df['teks_bersih'].head(3))

nama_fitur = ['Ada_URL', 'Jml_URL', 'Panjang_URL', 'Jml_Titik', 'Jml_Strip', 'Simbol_@', 'HTTPS', 'Pakai_IP']
df_cek = pd.DataFrame(hasil_fitur, columns=nama_fitur)
print(df_cek)