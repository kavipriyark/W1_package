from openai import OpenAI

client = OpenAI()

question = "YOUR CAPSTONE DOMAIN QUESTION HERE"

prompts = {
    "A": "You are concise.",
    "B": "You are a kindergarten teacher. Explain like the listener is five years old.",
    "C": "You are a Shakespearean poet. Reply in iambic verse where possible.",
    "D": "You are a brilliant but impatient physicist. You explain accurately but you don't have time for niceties.",
}

for name, system in prompts.items():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.7,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": question},
        ],
    )
    print(f"\nPrompt {name}: {system}")
    print(response.choices[0].message.content)
