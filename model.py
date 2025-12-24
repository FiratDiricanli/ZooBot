import pickle
from data import egitim_verisi
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
import numpy as np

# ----------------------------------------------------
# 1. KRİTİK TOKENİZER FONKSİYONU
# ----------------------------------------------------
# Bu fonksiyon, pickle hatası vermemek için tanımlı olmalıdır.
def tokenize_ve_kok_bul(metin):
    return metin.lower().split()

print("Model eğitiliyor...")

# Veri Hazırlama
X_egitim = []
y_egitim = []

for intent in egitim_verisi["intentler"]:
    for ornek in intent["ornekler"]:
        X_egitim.append(ornek)
        y_egitim.append(intent["tag"])

# Label Encoder
le = LabelEncoder()
y_egitim_sayisal = le.fit_transform(y_egitim)

# ----------------------------------------------------
# 2. PIPELINE TANIMI (Agresif Ayar)
# ----------------------------------------------------
# N-gram ve C=10.0 ile niyet ayrımcılığını keskinleştiriyoruz.
# model.py'deki Pipeline tanımı:
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 3))), 
    ('svc', SVC(kernel='linear', probability=True, C=10.0)) # <-- C=10.0 OLMALI
])

# 3. Modeli Eğitme
pipeline.fit(X_egitim, y_egitim_sayisal)

# 4. Modeli ve Label Encoder'ı Kaydetme (YENİ İSİMLERLE)
with open('yeni_model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)
    
with open('yeni_le.pkl', 'wb') as f:
    pickle.dump(le, f)

print("Model başarıyla eğitildi!")
print("Model ve Label Encoder 'yeni_model.pkl' ve 'yeni_le.pkl' dosyalarına kaydedildi.")