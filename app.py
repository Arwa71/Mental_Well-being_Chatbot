# import streamlit as st
# import requests
# import time
# import random
# import openai 


# # Set Fullscreen Mode
# # st.set_page_config(page_title="Mental Well-being Chatbot", layout="wide")

# # Load external CSS file
# with open("style.css") as css_file:
#     st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# # HEADER
# st.markdown("<div class='header'>", unsafe_allow_html=True)
# st.markdown("<h1 id='s1'> Mental Well-being Chatbot🗣️✨</h1>", unsafe_allow_html=True)
# st.markdown("<p> I'm here to listen. How are you feeling today?</p>", unsafe_allow_html=True)
# st.markdown("</div>", unsafe_allow_html=True)

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Chat Display Box
# st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
# for msg in st.session_state.messages:
#     sender_class = "chat-bubble-user" if msg["sender"] == "user" else "chat-bubble-bot"
#     st.markdown(f"<div class='{sender_class}'>{msg['text']}</div>", unsafe_allow_html=True)
# st.markdown("</div>", unsafe_allow_html=True)


# # User input box
# user_input = st.chat_input("Express your feeling here...")

# if user_input:
#     # Add user message to chat history
#     st.session_state.messages.append({"sender": "user", "text": user_input})

#     # Display user message
#     st.markdown(f"<div class='chat-bubble-user'>{user_input}</div>", unsafe_allow_html=True)

#     # Simulate bot typing
#     with st.spinner("🤖 Typing..."):
#         time.sleep(2)  # Simulate delay

#         # Send request to Flask chatbot backend
#         response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_input}).json()
#         bot_reply = response.get("response", "I'm here to listen. Tell me more.")

#     # Display bot response
#     st.markdown(f"<div class='chat-bubble-bot'>{bot_reply}</div>", unsafe_allow_html=True)

#     # Add bot response to chat history
#     st.session_state.messages.append({"sender": "bot", "text": bot_reply})

# # SIDEBAR - Self-Care Tools
# st.sidebar.image("img1.png")

# st.sidebar.title(" Self-Care Tools 🌟💖")

# # ⿡ GUIDED MEDITATION
# if st.sidebar.button("🎧 Guided Meditation"):
#     st.sidebar.markdown("[🎧 Click here for Guided Meditation](https://www.youtube.com/watch?v=your_video_id)", unsafe_allow_html=True)

#     # st.sidebar.audio("guided_meditation.mp3")  # Replace with your meditation file

# # ⿢ JOURNALING SPACE
# st.sidebar.subheader("📝 Daily Journal")
# journal_entry = st.sidebar.text_area("Write your thoughts here...")
# if st.sidebar.button("Save Journal Entry"):
#     with open("journal.txt", "a") as file:
#         file.write(journal_entry + "\n---\n")
#     st.sidebar.success("📖 Journal entry saved!")
# # Redirect Button to Journal History Page


# # ⿣ MOOD TRACKER
# st.sidebar.subheader("📊 Mood Tracker")
# mood = st.sidebar.selectbox("How are you feeling today?", ["😊 Happy", "😞 Sad", "😡 Angry", "😨 Anxious", "😌 Relaxed"])
# if st.sidebar.button("Log Mood"):
#     with open("mood_log.txt", "a", encoding="utf-8") as file:

    
#         file.write(mood + "\n")
#     st.sidebar.success("✅ Mood logged!")

# # ⿦ MOTIVATIONAL QUOTES
# quotes = [
#     "💡 'You are stronger than you think.'",
#     "🌈 'This too shall pass.'",
#     "🌿 'Breathe. You got this.'",
#     "💖 'Your feelings are valid.'"
# ]
# st.sidebar.subheader("🌟 Daily Motivation")
# st.sidebar.write(random.choice(quotes))




# # Example Usage


# # ⿤ BREATHING EXERCISE
# if st.sidebar.button("🫁 Breathing Exercise"):
#     st.sidebar.write("🫁 Inhale for 4 seconds... Hold for 4 seconds... Exhale for 4 seconds...")
#     st.sidebar.image("niece-cute.gif")  # Replace with a real breathing GIF

# # ⿥ CRISIS HELPLINE
# st.sidebar.subheader("📞 Emergency Helplines")
# st.sidebar.write("💙 Need urgent help? Call a professional now.")
# st.sidebar.write("📞 *Mental Health Helpline*: 1800-599-0019")
# st.sidebar.write("🌍 [Find a helpline near you](https://findahelpline.com)")





import streamlit as st
import requests
import time
import random
# import openai

# Load external CSS file
with open("style.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# HEADER
st.markdown("<div class='header'>", unsafe_allow_html=True)
st.markdown("<h1 id='s1'> Mental Well-being Chatbot🗣️✨</h1>", unsafe_allow_html=True)
st.markdown("<p> I'm here to listen. How are you feeling today?</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Display Box
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
for msg in st.session_state.messages:
    sender_class = "chat-bubble-user" if msg["sender"] == "user" else "chat-bubble-bot"
    st.markdown(f"<div class='{sender_class}'>{msg['text']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# User input box (with unique key to avoid duplicate ID error)
user_input = st.chat_input("Express your feeling here...", key="main_chat_box")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"sender": "user", "text": user_input})

    # Display user message
    st.markdown(f"<div class='chat-bubble-user'>{user_input}</div>", unsafe_allow_html=True)

    # Simulate bot typing
    with st.spinner("🤖 Typing..."):
        time.sleep(2)  # Simulate delay

        try:
            # Send request to Flask chatbot backend
            response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_input}).json()
            bot_reply = response.get("response", "I'm here to listen. Tell me more.")
        except requests.exceptions.ConnectionError:
            bot_reply = "⚠️ Cannot connect to the chatbot backend. Please ensure your Flask server is running."

    # Display bot response
    st.markdown(f"<div class='chat-bubble-bot'>{bot_reply}</div>", unsafe_allow_html=True)

    # Add bot response to chat history
    st.session_state.messages.append({"sender": "bot", "text": bot_reply})

# SIDEBAR - Self-Care Tools
st.sidebar.image("img1.png")
st.sidebar.title(" Self-Care Tools 🌟💖")

# 🎧 Guided Meditation
if st.sidebar.button("🎧 Guided Meditation"):
    st.sidebar.markdown("[🎧 Click here for Guided Meditation](https://www.youtube.com/watch?v=your_video_id)", unsafe_allow_html=True)

# 📝 Daily Journal
st.sidebar.subheader("📝 Daily Journal")
journal_entry = st.sidebar.text_area("Write your thoughts here...")
if st.sidebar.button("Save Journal Entry"):
    with open("journal.txt", "a", encoding="utf-8") as file:
        file.write(journal_entry + "\n---\n")
    st.sidebar.success("📖 Journal entry saved!")

# 📊 Mood Tracker
st.sidebar.subheader("📊 Mood Tracker")
mood = st.sidebar.selectbox(
    "How are you feeling today?",
    ["😊 Happy", "😞 Sad", "😡 Angry", "😨 Anxious", "😌 Relaxed"]
)
if st.sidebar.button("Log Mood"):
    with open("mood_log.txt", "a", encoding="utf-8") as file:
        file.write(mood + "\n")
    st.sidebar.success("✅ Mood logged!")

# 🌟 Daily Motivation
quotes = [
    "💡 'You are stronger than you think.'",
    "🌈 'This too shall pass.'",
    "🌿 'Breathe. You got this.'",
    "💖 'Your feelings are valid.'"
]
st.sidebar.subheader("🌟 Daily Motivation")
st.sidebar.write(random.choice(quotes))

# 🫁 Breathing Exercise
if st.sidebar.button("🫁 Breathing Exercise"):
    st.sidebar.write("🫁 Inhale for 4 seconds... Hold for 4 seconds... Exhale for 4 seconds...")
    st.sidebar.image("niece-cute.gif")  # Replace with a real breathing GIF

# 📞 Crisis Helplines
st.sidebar.subheader("📞 Emergency Helplines")
st.sidebar.write("💙 Need urgent help? Call a professional now.")
st.sidebar.write("📞 *Mental Health Helpline*: 1800-599-0019")
st.sidebar.write("🌍 [Find a helpline near you](https://findahelpline.com)")
