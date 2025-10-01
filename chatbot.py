import google.generativeai as genai
import streamlit as st

GOOGLE_API_KEY = "AIzaSyAMQiaYoAZBEu0aCttiK3y_3iL6fd_-r1s"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def get_chatbot_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {e}"

st.set_page_config(page_title="Sage Chatbot", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f0f2f6;
    }
    .chat-box {
        max-width: 700px;
        margin: auto;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
    }
    .user-message {
        background-color: #d1e7dd;
        color: #155724;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        text-align: right;
    }
    .bot-message {
        background-color: #f8d7da;
        color: #721c24;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        text-align: left;
    }
    .chat-header {
        text-align: center;
        color: #343a40;
    }
    .send-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .send-button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='chat-header'>🤖 Sage Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Powered by Google Gemini Model. Chat with AI!</p>", unsafe_allow_html=True)
st.write("---")

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.header("💡 Chatbot Settings")
    bot_name = st.text_input("Bot Name", value="Sage")
    st.write(f"Current Bot Name: **{bot_name}**")
    st.write("---")
    st.info("This chatbot uses Google Gemini API to provide intelligent responses. Customize the name and enjoy chatting!")

def display_chat():
    st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
    for chat in st.session_state.history:
        if chat["is_user"]:
            st.markdown(f"<div class='user-message'><strong>You:</strong> {chat['message']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-message'><strong>{bot_name}:</strong> {chat['message']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def main():
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("You:", key="input", placeholder="Type your message here...", label_visibility="hidden")
        submit_button = st.form_submit_button("Send")

        if submit_button and user_input:
            st.session_state.history.append({"message": user_input, "is_user": True})

            bot_response = get_chatbot_response(user_input)
            st.session_state.history.append({"message": bot_response, "is_user": False})

    if st.session_state.history:
        display_chat()

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 14px;'>"
    "Powered by Streamlit • Designed with ❤️ by Sage</p>",
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()

