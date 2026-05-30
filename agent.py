from openai import OpenAI

client = OpenAI(api_key="APfrom openai import OpenAI

client = OpenAI(api_key="API_KEY_KAMU")

while True:
    user = input("Anda: ")

    if user.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role":"system","content":"Kamu adalah AI Agent."},
            {"role":"user","content":user}
        ]
    )

    print(response.choices[0].message.content)")

while True:
    user = input("Anda: ")

    if user.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role":"system","content":"Kamu adalah AI Agent."},
            {"role":"user","content":user}
        ]
    )

    print(response.choices[0].message.content)
