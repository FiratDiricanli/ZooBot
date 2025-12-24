# 🦅 ZooBot/EN

*ZooBot* is an AI-powered chatbot designed to answer questions about animals, compare their characteristics, and manage conversation history. It uses *Machine Learning (Scikit-learn)* for intent recognition and *Flask* for the web interface.

## 🚀 Features

* *Smart Responses:* Understands questions about diet, habitat, lifespan, and abilities.
* *Dynamic Comparisons:* Can compare animals based on real data (e.g., "Is a lion faster than a tiger?").
* *Chat History:* Saves and retrieves past conversations using *SQLite*.
* *Web Interface:* Features a user-friendly chat interface.

## 🛠️ Installation and Usage

1.  *Install Dependencies:*
    bash
    pip install -r requirements.txt
    

2.  *Train the Model:*
    (You need to run this once to generate the AI model files)
    bash
    python model.py
    

3.  *Run the Application:*
    bash
    python app.py
    

4.  *Open in Browser:*
    Go to http://127.0.0.1:5002 to start chatting!

## 📂 Project Structure

* app.py: Main application file.
* model.py: Training script for the NLP (Natural Language Processing) model.
* data.py: Training data and intent definitions.
* knowledge_base.py: Database of animal information.



# 🦅 ZooBot/TR

*ZooBot, hayvanlar hakkındaki soruları yanıtlamak, onların özelliklerini karşılaştırmak ve konuşma geçmişini yönetmek için tasarlanmış, yapay zeka destekli bir sohbet botudur. Niyet tanıma (intent recognition) için **Makine Öğrenimi (Scikit-learn)* ve web arayüzü için *Flask* kullanır.

## 🚀 Özellikler

* *Akıllı Yanıtlar:* Beslenme, yaşam alanı, ömür ve yetenekler hakkındaki soruları anlar.
* *Dinamik Karşılaştırmalar:* Hayvanları gerçek verilere dayanarak karşılaştırabilir (Örn: "Bir aslan bir kaplandan daha hızlı mıdır?").
* *Sohbet Geçmişi:* Geçmiş konuşmaları *SQLite* kullanarak kaydeder ve geri getirir.
* *Web Arayüzü:* Kullanıcı dostu bir sohbet arayüzüne sahiptir.

## 🛠️ Kurulum ve Kullanım

1.  *Bağımlılıkları Kurun:*
    bash
    pip install -r requirements.txt
    

2.  *Modeli Eğitin:*
    (Yapay zeka model dosyalarını oluşturmak için bunu bir kez çalıştırmanız gerekir)
    bash
    python model.py
    

3.  *Uygulamayı Çalıştırın:*
    bash
    python app.py
    

4.  *Tarayıcıda Açın:*
    Sohbete başlamak için http://127.0.0.1:5002 adresine gidin!

## 📂 Proje Yapısı

* app.py: Ana uygulama dosyası.
* model.py: NLP (Doğal Dil İşleme) modelini eğitme betiği.
* data.py: Eğitim verileri ve niyet tanımlamaları.
* knowledge_base.py: Hayvan bilgilerinin veritabanı.
