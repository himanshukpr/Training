import ollama

model_name = "llama3.2:latest"
# prompt = "Tell me a short story about a talking cat."
prompt = input("Enter your prompt: ")

response = ollama.generate(model=model_name, prompt=prompt)
print(response['response'])