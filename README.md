# 🦁 ZooBot

**ZooBot** is an AI-powered chatbot designed to answer questions about animals, compare their characteristics, and manage conversation history. It uses **Machine Learning (Scikit-learn)** for intent recognition and **Flask** for the web interface.

## 🚀 Features

* **Smart Responses:** Understands questions about diet, habitat, lifespan, and abilities.
* **Dynamic Comparisons:** Can compare animals based on real data (e.g., *"Is a lion faster than a tiger?"*).
* **Chat History:** Saves and retrieves past conversations using **SQLite**.
* **Web Interface:** Features a user-friendly chat interface.

## 🛠️ Installation and Usage

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Train the Model:**
    *(You need to run this once to generate the AI model files)*
    ```bash
    python model.py
    ```

3.  **Run the Application:**
    ```bash
    python app.py
    ```

4.  **Open in Browser:**
    Go to `http://127.0.0.1:5002` to start chatting!

## 📂 Project Structure

* `app.py`: Main application file.
* `model.py`: Training script for the NLP (Natural Language Processing) model.
* `data.py`: Training data and intent definitions.
* `knowledge_base.py`: Database of animal information.
