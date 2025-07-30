import streamlit as st

import ollama
import time
model_name = "llama3.2:latest"



if 'chats' not in st.session_state:
    st.session_state.chats = []
if 'gpt_chat' not in st.session_state:
     st.session_state.gpt_chat = []

st.set_page_config(page_title="Doctor's App")
st.title("Doctor's App")

hide_streamlit_scrollbar = """
<style>
    
    /* Target the element containing the sidebar content */
    div[data-testid="stSidebarContent"] {
        overflow-y: hidden !important;
    }
    .stButton>button
    {
    width: 100%;
    }
</style>
"""

st.markdown(hide_streamlit_scrollbar, unsafe_allow_html=True)


add_button = st.sidebar.button('New Chat',key='chat')


st.sidebar.subheader('Chat History')
container = st.sidebar.container(height=300)

with container:
    if add_button:
        st.session_state.chats.append('Chat {}'.format(len(st.session_state.chats) + 1))
    
    for chat in st.session_state.chats:
            container.write(chat)
    

delete_Button = st.sidebar.button('Clear History')
if delete_Button:
    container.empty()
    for chat in st.session_state.chats:
        st.session_state.chats.clear()

        

st.sidebar.divider()

version = st.sidebar.selectbox('GPT Version', ['v1.0', 'v2.0', 'v3.0'], key='version')
st.sidebar.divider()
st.sidebar.chat_message('User').write('Hi, Himanshu!')

st.write("Welcome to the Doctor's App you are using {}".format(version))


message = st.container(height=600)

prompt = st.chat_input(placeholder="Type your message here...")
if prompt:
    st.session_state.gpt_chat.append({"role": "user", "content": prompt})
    response = ollama.generate(model=model_name, prompt=prompt)
    st.session_state.gpt_chat.append({"role": "ai", "content": f"{response['response']}", "complete": False})

with message:
    for p in st.session_state.gpt_chat:
        # message.chat_message(p['role']).write(p['content'])

        if p['role'] == 'user':
            st.chat_message(p['role']).write(p['content'])
        else:
            # Assuming 'ai' role for the response
            with st.chat_message(p['role']):
                typing_placeholder = st.empty()
                typing_text = ""
                if not p['complete']:
                    for char in p['content']:
                        typing_placeholder.write(typing_text + char)
                        typing_text += char
                        time.sleep(0.05)
                else:
                    typing_placeholder.write(p['content'])

                p['complete'] = True
