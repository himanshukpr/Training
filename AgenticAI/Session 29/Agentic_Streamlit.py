import streamlit as st
import datetime
import time
from pymongo import MongoClient
from openai import OpenAI
import json

# section 1
# MONGO_db_URI = 'mongodb+srv://admin:admin@cluster0.blirv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
MONGO_db_URI = st.secrets['MONGO_URI']
OPEN_AI = st.secrets['OPEN_AI_KEY']  # Assuming OPEN_AI_KEY is stored in Streamlit secrets

# section 2
client = MongoClient(MONGO_db_URI)
db = client['aiPatientDB']
patients_collection = db['patients']
consultations_collection = db['consultations']
selected_model = "gpt-4o-mini"

# section 3
openai_client = OpenAI(api_key=OPEN_AI)

# section 4
st.set_page_config(page_title='Doctor Assistant', page_icon=':hospital:', layout='wide')
st.title('Doctor Assistant :hospital:')

# section 5
def get_patient_by_phone(phone):
    query = {'phone': phone}
    documents = patients_collection.find(query)
    if len(documents) > 0:
        return documents[0]
    
def add_patient(name, phone, email):
    patient = patients_collection.find_one({'phone': phone})
    if patient:
        return 'Patient {} already exists with phone {}. Would you like to write the consultation instead?'.format(name, phone)
    patient = {
        'name': name,
        'phone': phone,
        'email': email,
        'created_at': datetime.datetime.now()
    }
    result = patients_collection.insert_one(patient)
    if result.inserted_id:
        return '{} added successfully with {}'.format(name,phone)
    
def save_consultation(phone, medicines, remarks):
    query=  {
        'phone': phone,
        'medicines': medicines,
        'remarks': remarks,
        'created_at': datetime.datetime.now()
    }
    result = consultations_collection.insert_one(query)
    if result.inserted_id:
        return 'Consultation saved successfully for {}'.format(phone)
    else:
        return 'Failed to save consultation for {}'.format(phone)
def fetch_consultation(phone):
    pass



if 'messages' not in st.session_state:
    st.session_state.messages = []

def ai_response(user_message):
    tools =   [
                {
                    "type": "function",
                    "function":{
                        "name": "add_patient",
                        "description": "Add a new patient in database",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "phone": {"type": "string"},
                                "email": {"type": "string"}
                            },
                            "required": ["name", "phone", "email"],
                        }
                    }
                },
                {
                    "type": "function",
                    "function":{
                        "name": "save_consultation",
                        "description": "Add a new consultation of a ptient in database",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "phone": {"type": "string"},
                                "medicines": {"type": "string"},
                                "remarks": {"type": "string"},
                            },
                            "required": ["phone", "medicines"],
                    }
                }
            }

        ]


    response = openai_client.chat.completions.create(
        model=selected_model,
        messages=[
            # this is the role as doctors assistant
                {"role": "system", "content": 'You are stictly a doctors assistant you cannot give the response on anything else, and you are a assistant who can create patients and save the consultation of a patient in the mongoDB. And also use the phone number as a unique identifier for the patient key and also write the medicines if you think it is necessary.'},
                *[{'role': msg['role'], 'content': msg['content']} for msg in st.session_state.messages],
                {"role": "user", "content": user_message}
            ],
        tools=tools
    ) 
    print('[Doctors Assistant AI App] response:', response)
    choice = response.choices[0]
    print('[Doctors Assistant AI App] choice:', choice)
    
    if choice.finish_reason == 'tool_calls':
        function_name = choice.message.tool_calls[0].function.name
        arguments = choice.message.tool_calls[0].function.arguments
        # JSON to Dictionary
        # i.e. string representation of dicionary which is JSON
        # to python dictionary
        arguments = json.loads(arguments)
        # json.dumps -> convert python dictionary into JSON
        if function_name == 'add_patient':
            return add_patient(**arguments)
        elif function_name == 'save_consultation':
            return save_consultation(**arguments)
    else:
        return "I cannot process your input. please try agian !"



user_input = st.chat_input(placeholder="Type your message here...", key="user_input")

if user_input:

    st.session_state.messages.append({'role': 'user', 'content': user_input})            
    st.session_state.messages.append({'role': 'assistant', 'content': ai_response(user_input), 'complete': False})

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
                    time.sleep(0.02)
            else:
                typing_placeholder.write(msg['content'])

            msg['complete'] = True
            


