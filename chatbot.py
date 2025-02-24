import nltk
import random

# Download NLTK data (only needed once)
nltk.download('punkt')

# Predefined symptoms and responses
symptoms = {
    "fever": "It might be a sign of flu or infection. Stay hydrated and monitor your temperature.",
    "cough": "A cough can be due to a cold, allergies, or respiratory infection.",
    "headache": "Headaches can be caused by stress, dehydration, or migraines.",
    "stomach pain": "This could be due to indigestion, food poisoning, or other conditions."
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for symptom in symptoms:
        if symptom in user_input:
            return symptoms[symptom]
    return "I'm not sure about that. Please consult a doctor for accurate advice."

# Chatbot loop
print("Medical Chatbot: Hello! What symptoms are you experiencing?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Medical Chatbot: Take care! Goodbye.")
        break
    response = chatbot_response(user_input)
    print("Medical Chatbot:", response)
