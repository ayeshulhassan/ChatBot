import streamlit as st
import google.generativeai as genai

# Set up Google API key
GOOGLE_API_KEY = "AIzaSyAveYjOncVL_R0ftzl-BXzzZ1u5_6tLFew"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def GetResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Initialize conversation history in Streamlit session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Set page config
st.set_page_config(page_title="ᴅɪᴀʟᴏɢɪx", layout="centered")
st.title("💬 ᴅɪᴀʟᴏɢɪx")
st.write("ᴘᴏᴡᴇʀᴇᴅ ʙʏ **ɢᴇᴍɪɴɪ-𝟷.𝟻-ғʟᴀsʜ**")

# Chat form for user input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here:", max_chars=2000)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = GetResponseFromModel(user_input)
            # Add user input and bot response to the conversation history
            st.session_state.conversation_history.append(("User", user_input))
            st.session_state.conversation_history.append(("Bot", response))
        else:
            st.warning("Please enter a prompt.")

# Display conversation history
st.write("### Conversation History:")
for sender, message in st.session_state.conversation_history:
    st.write(f"**{sender}:** {message}")

# Add custom CSS for better styling
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #007BFF;
        color: white;
        font-weight: bold;
    }
    .stTextInput > div > input {
        padding: 10px;
        font-size: 16px;
        border: 2px solid #007BFF;
        border-radius: 5px;
    }
    .stTextInput > div > input:focus {
        border-color: #0056b3;
        box-shadow: 0 0 5px #0056b3;
    }
    .stTextInput > div > label {
        font-weight: bold;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)
