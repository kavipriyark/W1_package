from openai import OpenAI

client = OpenAI()

def chat(messages, model="gpt-4o-mini", temperature=0.7):
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=messages,
    )
    return response.choices[0].message.content

messages = [
    {"role": "system", "content": "You are a concise assistant."},
    {"role": "user", "content": "My name is Kavipriya and I am learning RAG."},
    {"role": "assistant", "content": "Nice to meet you, Kavipriya! RAG is a great topic to learn."},
    {"role": "user", "content": "What is my name and what am I learning?"},
]

print("WITH history:")
print(chat(messages))

# Control: same final question, but without the earlier exchange
print("\nWITHOUT history:")
print(chat([
    {"role": "system", "content": "You are a concise assistant."},
    {"role": "user", "content": "What is my name and what am I learning?"},
]
)
)