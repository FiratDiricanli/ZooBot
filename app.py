from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import random
import fuzzywuzzy.fuzz
import sqlite3
import json
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ----------------------------------------------------
# 🔒 GÜVENLİK AYARLARI
# ----------------------------------------------------
# .env dosyasındaki şifreleri yükle
load_dotenv()

# API anahtarını güvenli dosyadan çek
MY_API_KEY = os.getenv("GOOGLE_API_KEY")

# ----------------------------------------------------
# 🧠 AKILLI MODEL SEÇİCİ (OTOMATİK)
# ----------------------------------------------------
try:
    if not MY_API_KEY or "BURAYA" in str(MY_API_KEY):
        print("UYARI: API Anahtarı bulunamadı! .env dosyanı kontrol et.")
    
    genai.configure(api_key=MY_API_KEY)
    
    # Mevcut modelleri listele ve çalışanı seç
    try:
        print("Google'dan model listesi alınıyor...")
        aktif_modeller = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # Öncelik sırasına göre en iyi modeli seç
        secilen_model = None
        if 'models/gemini-1.5-flash' in aktif_modeller:
            secilen_model = 'gemini-1.5-flash'
        elif 'models/gemini-pro' in aktif_modeller:
            secilen_model = 'gemini-pro'
        elif aktif_modeller:
            # Listede ne varsa ilkini al (models/ kısmını atarak)
            secilen_model = aktif_modeller[0].replace('models/', '')
        else:
            secilen_model = 'gemini-1.5-flash' # Liste boşsa şansımızı bununla deneyelim

        print(f"✅ BAŞARILI: '{secilen_model}' modeli kullanılıyor.")
        model_gemini = genai.GenerativeModel(secilen_model)

    except Exception as e_list:
        print(f"⚠️ Model listesi alınamadı, varsayılan deneniyor: {e_list}")
        model_gemini = genai.GenerativeModel('gemini-1.5-flash')

except Exception as e:
    print(f"API Bağlantı Hatası: {e}")

# ----------------------------------------------------
# VERİTABANI VE MODEL
# ----------------------------------------------------
from data import egitim_verisi
from knowledge_base import HAYVAN_BILGILERI 

DATABASE = 'chatbot_gecmis.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS sohbetler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            baslik TEXT NOT NULL,
            gecmis TEXT NOT NULL,
            tarih TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def tokenize_ve_kok_bul(metin):
    return metin.lower().split()

try:
    with open('yeni_model.pkl', 'rb') as f:
        pipeline = pickle.load(f) 
    with open('yeni_le.pkl', 'rb') as f:
        le = pickle.load(f)
except FileNotFoundError:
    print("Model dosyaları yok. Önce 'python model.py' çalıştır.")

def varlik_tanima(soru):
    hayvan_isimleri = list(HAYVAN_BILGILERI.keys())
    bulunan_hayvanlar = []
    for hayvan in hayvan_isimleri:
        if fuzzywuzzy.fuzz.partial_ratio(hayvan, soru.lower()) >= 80:
            if hayvan not in bulunan_hayvanlar:
                bulunan_hayvanlar.append(hayvan)
    if len(bulunan_hayvanlar) > 1: return bulunan_hayvanlar
    elif len(bulunan_hayvanlar) == 1: return bulunan_hayvanlar[0]
    return None

# ----------------------------------------------------
# GEMINI FONKSİYONU
# ----------------------------------------------------
def geminiye_sor(soru):
    try:
        print(f"Gemini'ye soruluyor: {soru}") 
        prompt = f"Sen ZooBot adında uzman bir asistansın. Türkçe cevapla. Soru: {soru}"
        response = model_gemini.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"🛑 GEMINI HATASI: {e}")
        return f"Hata oluştu: {str(e)}"

# ----------------------------------------------------
# ANA MANTIK
# ----------------------------------------------------
def yz_botu_yanitla(kullanici_sorusu):
    try:
        tahmin_olasiliklari = pipeline.predict_proba([kullanici_sorusu])[0]
        en_yuksek_olasilik = np.max(tahmin_olasiliklari)
        tahmin_sonucu = pipeline.predict([kullanici_sorusu])
        tahmin_niyeti = le.inverse_transform(tahmin_sonucu)[0]
    except:
        en_yuksek_olasilik = 0
        tahmin_niyeti = "bilinmiyor"

    hayvan_varliklari = varlik_tanima(kullanici_sorusu)
    hayvan_adi = hayvan_varliklari[0] if isinstance(hayvan_varliklari, list) else hayvan_varliklari

    ozel_niyetler = ["niyet_takim", "niyet_sadik", "niyet_kim", "merhaba", "nasılsın", "hos_cakal"]
    if tahmin_niyeti in ozel_niyetler and en_yuksek_olasilik > 0.6:
        for intent in egitim_verisi["intentler"]:
            if intent["tag"] == tahmin_niyeti:
                return random.choice(intent["cevaplar"])

    if hayvan_adi and tahmin_niyeti in ["beslenme", "yasama_alani", "omur", "hiz"]:
        try:
            return HAYVAN_BILGILERI[hayvan_adi][tahmin_niyeti]
        except:
            pass 

    return geminiye_sor(kullanici_sorusu)

# ----------------------------------------------------
# FLASK
# ----------------------------------------------------
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    kullanici_mesaji = request.json.get('message', '')
    bot_yaniti = yz_botu_yanitla(kullanici_mesaji)
    return jsonify({'response': bot_yaniti})

@app.route('/api/chats', methods=['GET'])
def get_chats():
    conn = get_db_connection()
    chats = conn.execute("SELECT id, baslik, strftime('%d.%m.%Y %H:%M', tarih) as tarih_okunur FROM sohbetler ORDER BY id DESC").fetchall()
    conn.close()
    return jsonify([dict(chat) for chat in chats])

@app.route('/api/chat/<int:chat_id>', methods=['GET'])
def load_chat(chat_id):
    conn = get_db_connection()
    chat = conn.execute('SELECT gecmis FROM sohbetler WHERE id = ?', (chat_id,)).fetchone()
    conn.close()
    return jsonify(json.loads(chat['gecmis'])) if chat else (jsonify({'error': 'Bulunamadı'}), 404)

@app.route('/api/save', methods=['POST'])
def save_chat():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO sohbetler (baslik, gecmis, tarih) VALUES (?, ?, datetime("now", "localtime"))', (data.get('baslik'), json.dumps(data['gecmis'])))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Kaydedildi'}), 201

@app.route('/api/chat/<int:chat_id>', methods=['DELETE'])
def delete_chat(chat_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM sohbetler WHERE id = ?', (chat_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Silindi'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5002, use_reloader=False)