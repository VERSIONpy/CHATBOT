

responses = {}

with open(r"S:\HELL\CHATBOT\responses.txt","r") as file:
    for line in file:
        if ":" in line:
            key,value = line.strip().split(":",1)
            responses[key.strip().lower()] = value.strip()

print("Loaded keys:", list(responses.keys()))

while True:
    user_input = input("You: ").strip().lower()
    if user_input in responses:
        print("VERSION: " + responses[user_input])
        if user_input == "bye":   
            break
    else:
        print("VERSION:" + responses.get("unknown"))
        