"""
    software solution
    model view controller architecture

    agentic ai
    (AI model, goal and task) -> controller
    (streamlit chat ui) -> view
    (any data to be saved in dictionary) -> model

    in python 
    model is dictionary itself
"""

import streamlit as st
import time

st.set_page_config(page_icon="🩺", page_title="Chat UI")


st.title("Chat UI Demo")
st.subheader("Ask a question and get a response")

dataset = {
    'python': 'Python is a programming language.',
    'streamlit': 'Streamlit is a framework for building web apps with Python.',
    'ollama': 'Ollama is a tool for running large language models locally.',
    'agentic': 'Agentic AI is a framework for building AI agents that can perform tasks autonomously.'     
}


if 'messages' not in st.session_state:
    st.session_state.messages = []


user_input = st.chat_input(placeholder="Type your message here...", key="user_input")

if user_input:

    st.session_state.messages.append({'role': 'user', 'content': user_input})
    keywords = user_input.split(" ")
    for key in keywords:
        if key in dataset:
            response = dataset[key]
            break
        else:
            response = "I don't know the answer to that question."

            
    st.session_state.messages.append({'role': 'ai', 'content': response, 'complete': False})



for msg in st.session_state.messages:
    if msg['role'] == 'user':
        st.chat_message(msg['role']).write(msg['content'])
    else:
        # Assuming 'ai' role for the response
        with st.chat_message(msg['role']):
            typing_placeholder = st.empty()
            typing_text = ""
            if not msg['complete']:
                for char in msg['content']:
                    typing_placeholder.write(typing_text + char)
                    typing_text += char
                    time.sleep(0.05)
            else:
                typing_placeholder.write(msg['content'])

            msg['complete'] = True
            

        
        # st.chat_message(msg['role']).write(msg['content'])
    
