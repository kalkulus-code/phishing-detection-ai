import re
from urllib.parse import urlparse
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

def bersihkan_teks(teks):
    if not isinstance(teks, str):
        return ""
    teks = teks.lower()
    teks = re.sub(r'\s+', ' ', teks).strip()
    return teks

class UrlFeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        fitur_list = []
        url_pattern = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'

        for teks in X:
            teks_str = str(teks)
            urls = re.findall(url_pattern, teks_str)

            if not urls:
                fitur_list.append([0, 0, 0, 0, 0, 0, 0, 0])
            else:
                url = urls[0]
                if not url.startswith('http'):
                    url_untuk_parse = 'http://' + url
                else:
                    url_untuk_parse = url

                try:
                    parsed = urlparse(url_untuk_parse)
                    domain = parsed.netloc
                except ValueError:
                    domain = url

                ada_url = 1
                jml_url = len(urls)
                panjang_url = len(url)
                jml_titik = url.count('.')
                jml_strip = url.count('-')
                simbol_at = 1 if '@' in url else 0
                is_https = 1 if url.startswith('https://') else 0
                pakai_ip = 1 if re.search(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', domain) else 0

                fitur_list.append([
                    ada_url, jml_url, panjang_url, jml_titik,
                    jml_strip, simbol_at, is_https, pakai_ip
                ])

        return np.array(fitur_list)