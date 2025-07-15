# 🩺 Disease Prediction and Prescription System

### 👨‍💻 Team Members
- Sanskriti (Me)
- Priyanshi
- Hasim

---

## 📌 Project Overview

This project aims to build a smart system that can **predict diseases** based on user-inputted symptoms and provide **prescription suggestions**. By combining **Natural Language Processing (NLP)** and **Machine Learning**, we enable fast, efficient, and accessible medical insights using text-based symptom descriptions.

---

## 🎯 Key Features

- Accepts symptoms in natural language form (e.g., "I have a headache and sore throat").
- Predicts **top 3 most probable diseases** based on input.
- Shows predictions only with **≥10% confidence** to maintain clarity.
- Designed to be deployed via a **Flask backend API** and a **Next.js frontend**.
- Lightweight ML model using **TF-IDF** and **Naive Bayes**, suitable for real-time inference.

---

## 🛠 Technology Stack

### ⚙️ Machine Learning & NLP
- **Pandas, NumPy** – Data handling and processing
- **Scikit-learn** – Model training and evaluation
- **TfidfVectorizer** – Feature extraction from text
- **Multinomial Naive Bayes** – Text classification model

### 🧠 Backend
- **Flask** – Python-based web framework for hosting APIs

### 💻 Frontend
- **Next.js** – React-based framework for frontend development

---

## 📁 Dataset

- Used a **synthetic dataset** (`synthetic_training_data_updated.csv`) containing sentence-like symptom descriptions and disease labels.
- All text is cleaned using regex-based methods to normalize user input.

---

## 🧪 Model Training & Evaluation

- Preprocessed user input with a custom cleaning function.
- Converted text to numerical vectors using TF-IDF with bi-grams.
- Trained a **Multinomial Naive Bayes classifier**.
- Achieved good performance in predicting diseases based on unseen test data.
---


## ✅ Conclusion

- Successfully built a working NLP pipeline to map symptom descriptions to likely diseases.
- Delivered a system that can serve real users through a web interface.
- Achieved efficient and fast predictions in real time.

---


## 📦 How to Run (Local)

1. Clone the repository
2. Install dependencies from `requirements.txt`
3. Run the Flask API
4. Launch the Next.js frontend
5. Start entering symptoms!

---

> 👩‍⚕️ *Disclaimer: This is an educational project and should not be used for real medical decisions.*

