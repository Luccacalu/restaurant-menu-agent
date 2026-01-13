import ollama

def generate_answer(prompt: str) -> str:
    response = ollama.chat(
        model="llama3.1:8b",
        options={"temperature": 0.2, "num_predict": 300},
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"]
