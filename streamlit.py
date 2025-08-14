from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
from characters.character import Character

load_dotenv()

st.title("Star Wars Character Search")

client = OpenAI()

MODEL = "gpt-4o-mini-2024-07-18"

SYSTEM_PROMPT = """
You are a helpful assistant that extracts character information from \
https://starwars.fandom.com/wiki/
"""

# st.session_state is a dictionary that stores the state of the application
# It is used to store the messages between the user and the assistant
# We need to initialize the message list for the chat interface if this is a new session
if "messages" not in st.session_state:
    st.session_state.messages = []

# We need to display the messages in the chat interface
# as new messages are added, we update session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# We need to append some system prompt to the message list
# st.session_state.messages.append({"role": "system", "content": SYSTEM_PROMPT})

# We need to get the user prompt
if prompt := st.chat_input("Ask about a character?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # User just indicates that the icon is a user
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
