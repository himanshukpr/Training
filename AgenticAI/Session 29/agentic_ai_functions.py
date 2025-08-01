from openai import OpenAI
client = OpenAI(api_key="your_openai_api_key_here")

def ai_response(user_message):
    tools = [{
    "type": "function",
    "name": "add_patient",
    "description": "Add a new patient in the mongoDB",
    "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                },
                "phone": {
                    "type": "string",
                },
                "email": {
                    "type": "string",
                }
            },
            "required": [
                "name","phone"
            ],
            "additionalProperties": False
        }
    },
    {
    "type": "function",
    "name": "save_consultation",
    "description": "Save a new consultation of a patient in the mongoDB",
    "parameters": {
            "type": "object",
            "properties": {
                "phone": {
                    "type": "string",
                },
                "medicines": {
                    "type": "string",
                },
                "remarks": {
                    "type": "string",
                }
            },
            "required": [
                "phone","medicines"
            ],
            "additionalProperties": False
        }
    }
    ]


    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
                {"role": "system", "content": 'You are a doctors agent who can create patients and save the consultation of a patient in the mongoDB'},
                {"role": "user", "content": user_message}
            ],
        tools=tools
    )


    response.tool_choice