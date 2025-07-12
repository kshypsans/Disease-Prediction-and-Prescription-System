from flask import Flask, request, jsonify
import pickle
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ----------------- Load Trained Model ------------------

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# ----------------- Text Cleaning Function ------------------

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    text = re.sub(r"\d+", "", text)      # remove numbers
    return text.strip()

# ----------------- Disease Information ------------------

disease_info = {
    "Malaria": {
        "description": "A mosquito-borne disease causing fever, chills, and flu-like symptoms.",
        "precautions": ["Use mosquito nets", "Take antimalarial meds", "Avoid stagnant water"],
        "diet": ["Hydrate well", "Eat fruits", "Light nutritious meals"],
        "rest": "Get adequate rest and avoid exertion."
    },
    "Common Cold": {
        "description": "A viral infection of the upper respiratory tract.",
        "precautions": ["Stay warm", "Avoid cold drinks", "Use tissues"],
        "diet": ["Ginger tea", "Warm soups", "Citrus fruits"],
        "rest": "Sleep well and stay hydrated."
    },
    "Dengue": {
        "description": "A viral infection from mosquito bites causing joint pain and fever.",
        "precautions": ["Avoid mosquito-prone areas", "Use repellents", "Wear long sleeves"],
        "diet": ["Papaya leaf juice", "Coconut water", "High-fluid diet"],
        "rest": "Plenty of rest and hydration."
    },
    "Typhoid": {
        "description": "A bacterial infection due to Salmonella typhi.",
        "precautions": ["Drink boiled water", "Avoid outside food", "Maintain hygiene"],
        "diet": ["Soft bland diet", "Bananas", "Boiled rice"],
        "rest": "Bed rest for at least 1-2 weeks."
    },
    "Arthritis": {
        "description": "Joint inflammation causing pain and stiffness.",
        "precautions": ["Avoid cold", "Use joint supports", "Gentle exercise"],
        "diet": ["Omega-3 foods", "Turmeric", "Leafy greens"],
        "rest": "Take breaks, avoid joint overuse."
    },
    "Migraine": {
        "description": "Recurrent headaches often with nausea and sensitivity to light.",
        "precautions": ["Avoid triggers", "Limit caffeine", "Stay hydrated"],
        "diet": ["Magnesium-rich foods", "Ginger", "B-complex vitamins"],
        "rest": "Rest in a dark, quiet place during attacks."
    },
    # Add more diseases as needed...
}

# ----------------- Prediction Route ------------------

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    print("📩 Received:", data)
    user_input = data.get("text", "")

    if not user_input:
        return jsonify({"error": "No input text provided"}), 400

    cleaned_input = clean_text(user_input)
    probs = model.predict_proba([cleaned_input])[0]
    top_indices = probs.argsort()[::-1]

    predictions = []
    for idx in top_indices:
        confidence = probs[idx] * 100
        if confidence < 10:
            continue
        disease = model.classes_[idx]
        info = disease_info.get(disease, {})
        predictions.append({
            "disease": disease,
            "confidence": round(confidence, 2),
            "description": info.get("description", "No info available."),
            "precautions": info.get("precautions", []),
            "diet": info.get("diet", []),
            "rest": info.get("rest", "No rest advice available.")
        })
        if len(predictions) >= 3:
            break
    print(predictions)
    return jsonify({"predictions": predictions})

# ----------------- Root Route ------------------

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the NLP Disease Prediction API."})

# ----------------- Run App ------------------

if __name__ == '__main__':
    app.run(debug=True)
