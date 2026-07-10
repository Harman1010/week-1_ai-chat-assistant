from core.llm import ask_ai

print("Welcome,I'm your AI Chat Assistant")
print("Write exit to finish the session")

def start_chat():
    while True:
        query = input("User: ").strip()
        if query.lower() == "exit":
            print("Thank you for your time!")
            break
        response = ask_ai(query)
        print(f"AI: {response}")