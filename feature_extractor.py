import re
import numpy as np
import pandas as pd
from urllib.parse import urlparse
from sklearn.base import BaseEstimator, TransformerMixin

class UrlFeatureExtractor(BaseEstimator, TransformerMixin):
    """
    Class khusus untuk mencari URL di dalam teks email/input,
    lalu mengekstrak ciri-ciri mencurigakan dari URL tersebut.
    """
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        features = []
        for text in X:
            text_str = str(text)
            # Cari semua link http/https atau www di dalam teks
            urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', text_str)
            
            if len(urls) > 0:
                # Ambil URL pertama untuk dianalisis
                url = urls[0]
                if not url.startswith('http'):
                    url = 'http://' + url
                
                parsed = urlparse(url)
                domain = parsed.netloc
                
                has_url = 1
                url_count = len(urls)
                url_length = len(url)
                dot_count = url.count('.')
                hyphen_count = url.count('-')
                at_symbol = 1 if '@' in url else 0
                is_https = 1 if url.startswith('https://') else 0
                # Cek apakah domain menggunakan alamat IP (contoh: http://192.168.1.1/login)
                has_ip = 1 if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', domain) else 0
            else:
                # Jika input hanya teks biasa tanpa URL
                has_url = 0
                url_count = 0
                url_length = 0
                dot_count = 0
                hyphen_count = 0
                at_symbol = 0
                is_https = 0
                has_ip = 0
                
            features.append([
                has_url, url_count, url_length, dot_count, 
                hyphen_count, at_symbol, is_https, has_ip
            ])
            
        return np.array(features)

def bersihkan_teks(text):
    """Membersihkan karakter aneh dan huruf kapital berlebih pada teks email."""
    text = str(text).lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text