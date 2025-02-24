from flask import Flask, request, jsonify, render_template
import nltk

# Download NLTK data
nltk.download('punkt')

app = Flask(__name__)

# Define chatbot responses
symptoms = {
    "fever": "It might be a sign of flu or infection. Stay hydrated and monitor your temperature.",
    "cough": "A cough can be due to a cold, allergies, or respiratory infection.",
    "headache": "Headaches can be caused by stress, dehydration, or migraines.",
    "stomach pain": "This could be due to indigestion, food poisoning, or other conditions."
}

# Function to process user input
def chatbot_response(user_input):
    user_input = user_input.lower()
    for symptom in symptoms:
        if symptom in user_input:
            return symptoms[symptom]
    return "I'm not sure about that. Please consult a doctor for accurate advice."

# API endpoint for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = chatbot_response(user_message)
    return jsonify({"response": response})

# Web interface
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
