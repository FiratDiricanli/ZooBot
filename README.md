<div align="center">

# 🦅 ZooBot

**Yapay Zeka Destekli Hayvan Uzmanı / AI-Powered Animal Expert**

</div>

---

# 🇬🇧 ZooBot (English)

*ZooBot* is an AI-powered chatbot designed to answer questions about animals, compare their characteristics, and manage conversation history. It uses *Machine Learning (Scikit-learn)* for intent recognition and *Flask* for the web interface.

## 🚀 Features

* **Smart Responses:** Understands questions about diet, habitat, lifespan, and abilities.
* **Dynamic Comparisons:** Can compare animals based on real data (e.g., *"Is a lion faster than a tiger?"*).
* **Chat History:** Saves and retrieves past conversations using *SQLite*.
* **Web Interface:** Features a user-friendly chat interface.

## 🛠️ Installation and Usage

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
🔑 Setup API Key (Crucial Step):

Create a new file named .env in the main project folder.

Paste your Google Gemini API key inside it like this:

Ini, TOML

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
Train the Model: (Run this once to generate the AI model files)

Bash

python model.py
Run the Application:

Bash

python app.py
Start Chatting: Open your browser and go to: http://127.0.0.1:5002

📂 Project Structure
app.py: Main application file.

model.py: Training script for the NLP model.

data.py: Training data and intent definitions.

knowledge_base.py: Database of animal information.

🇹🇷 ZooBot (Türkçe)
ZooBot, hayvanlar hakkındaki soruları yanıtlamak, onların özelliklerini karşılaştırmak ve konuşma geçmişini yönetmek için tasarlanmış, yapay zeka destekli bir sohbet botudur. Niyet tanıma (intent recognition) için Makine Öğrenimi (Scikit-learn) ve web arayüzü için Flask kullanır.

🚀 Özellikler
Akıllı Yanıtlar: Beslenme, yaşam alanı, ömür ve yetenekler hakkındaki soruları anlar.

Dinamik Karşılaştırmalar: Hayvanları gerçek verilere dayanarak karşılaştırabilir (Örn: "Bir aslan bir kaplandan daha hızlı mıdır?").

Sohbet Geçmişi: Geçmiş konuşmaları SQLite kullanarak kaydeder ve geri getirir.

Web Arayüzü: Kullanıcı dostu bir sohbet arayüzüne sahiptir.

🛠️ Kurulum ve Kullanım
Gerekli Kütüphaneleri Kurun:

Bash

pip install -r requirements.txt
🔑 API Anahtarını Ayarlayın (Önemli):

Proje klasöründe .env adında yeni bir dosya oluşturun.

İçine Google Gemini API anahtarınızı şu şekilde yapıştırın:

Ini, TOML

GOOGLE_API_KEY="BURAYA_ANAHTARINIZI_YAZIN"
Modeli Eğitin: (Yapay zeka model dosyalarını oluşturmak için bunu bir kez çalıştırmanız gerekir)

Bash

python model.py
Uygulamayı Çalıştırın:

Bash

python app.py
Sohbete Başlayın: Tarayıcınızda şu adrese gidin: http://127.0.0.1:5002

📂 Proje Yapısı
app.py: Ana uygulama dosyası.

model.py: NLP modelini eğitme betiği.

data.py: Eğitim verileri ve niyet tanımlamaları.

knowledge_base.py: Hayvan bilgilerinin veritabanı.
