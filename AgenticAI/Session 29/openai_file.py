from openai import OpenAI
OPEN_AI_KEY = "sk-mnopqrstijkl5678mnopqrstijkl5678mnopqrst"
client = OpenAI(api_key=OPEN_AI_KEY)



response = client.responses.create(
    model="gpt-4o-mini",
    input="Tell me a bedtime story to help me sleep"
)

print(response.output_text)