# (venv1) PS C:\Users\richa\Downloads\2nd year_4_sem\mental> $env:GOOGLE_API_KEY='AIzaSyDFqB1tlHYzOGOeB7OCUZpZqtOPJevvBZ0'                                        
# (venv1) PS C:\Users\richa\Downloads\2nd year_4_sem\mental> python rich_back.py
#  * Serving Flask app 'rich_back'
#AIzaSyDFqB1tlHYzOGOeB7OCUZpZqtOPJevvBZ0
#AIzaSyDFqB1tlHYzOGOeB7OCUZpZqtOPJevvBZ0
# from flask import Flask, request, jsonify
# import os
# from google import genai  # Import the Google GenAI client

# app = Flask(__name__)

# # Load your Google API key from environment variable
# GOOGLE_API_KEY = os.getenv('AIzaSyDFqB1tlHYzOGOeB7OCUZpZqtOPJevvBZ0')

# # Initialize the Google GenAI client
# client = genai.Client(api_key=GOOGLE_API_KEY)

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_message = data.get('message')

#     # Prepare the request to Google GenAI service
#     try:
#         response = client.models.generate_content(
#             model="gemini-2.0-flash",
#             contents=user_message
#         )
#         bot_reply = response.text  # Get the generated response text
#     except Exception as e:
#         bot_reply = "Sorry, I couldn't process your request at the moment."

#     return jsonify({"response": bot_reply})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8509)  # Change the port if needed
#$env:GOOGLE_API_KEY='YOUR_ACTUAL_API_KEY'
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random
import re
# from google.generativeai import Client
from google import genai
# from google.generativeai import Client
 # Import the Google GenAI client

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Load your Google API key from environment variable
GOOGLE_API_KEY = os.getenv('AIzaSyDFqB1tlHYzOGOeB7OCUZpZqtOPJevvBZ0')  # Use the correct environment variable name

# Initialize the Google GenAI client
client = genai.Client(api_key=GOOGLE_API_KEY)

# Rule-based chatbot responses
responses = {
    "happy": ["That's great! 😊 Keep smiling!", "Happiness is contagious! Spread the joy!"],
    "sad": ["I'm here for you. 💙 Do you want to talk about it?", "It's okay to feel sad sometimes. Take your time."],
    "angry": ["Take a deep breath. 🫁 Anger is temporary.", "Would you like to try a relaxation technique?"],
    "anxious": ["Focus on your breathing. Inhale... Exhale... 🧘‍♂", "Try writing down your thoughts to ease your mind."],
    "relaxed": ["That's wonderful! 🌿 Stay in this peaceful moment.", "Relaxation is key to a healthy mind."]
}

# Keywords mapping for better emotion detection
emotion_keywords = {
    "happy": ["happy", "joy", "excited", "great", "awesome", "fantastic"],
    "sad": ["sad", "depressed", "unhappy", "cry", "down"],
    "angry": ["angry", "mad", "furious", "annoyed", "frustrated"],
    "anxious": ["anxious", "nervous", "stressed", "worried", "scared"],
    "relaxed": ["relaxed", "calm", "peaceful", "chill", "content"]
}

def detect_emotion(user_message):
    """Check if the user's message contains emotion-related words."""
    for mood, keywords in emotion_keywords.items():
        if any(re.search(rf"\b{word}\b", user_message, re.IGNORECASE) for word in keywords):
            return mood
    return None  # No matching emotion found

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    # Detect emotion from user message
    detected_mood = detect_emotion(user_message)
    
    if detected_mood:
        response = random.choice(responses[detected_mood])
    else:
        # If no emotion is detected, use Google GenAI for a response
        try:
            genai_response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=user_message
            )
            response = genai_response.text  # Get the generated response text
        except Exception as e:
            response = "Sorry, I couldn't process your request at the moment."

    return jsonify({"response": response, "emotion": detected_mood if detected_mood else "neutral"})

@app.route("/selfcare_suggestion", methods=["POST"])
def selfcare_suggestion():
    data = request.get_json()
    mood = data.get("mood", "neutral").lower()

    # AI-powered self-care suggestion
    suggestions = {
        "happy": "Celebrate your joy by sharing it with someone! 😊",
        "sad": "Write down your thoughts in a journal to feel lighter. 📝",
        "angry": "Try a deep breathing exercise to calm yourself. 🫁",
        "anxious": "Listen to a guided meditation to ease anxiety. 🎧",
        "relaxed": "Maintain this state with mindfulness exercises. 🌿"
    }

    suggestion = suggestions.get(mood, "Take a short walk to refresh your mind. 🚶‍♂")
    return jsonify({"suggestion": suggestion})

if __name__ == "__main__":
    app.run(debug=True)