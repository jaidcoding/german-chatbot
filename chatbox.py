import ollama

print("German chatbot is ready! Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Tschüss!")
        break

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system",
             "content": "You are a friendly German tutor who understands that the user is a beginner. Even if their German is broken or mixed with English, try your best to understand what they mean and respond naturally. Respond in simple German with an English translation in parentheses after each sentence. ONLY respond to what the user said. Ask ONE follow up question maximum. Never simulate a full conversation or speak for the user. Keep it to 2 sentences max."},
            {"role": "user",
             "content": user_input}
        ]
    )

    print("Bot:", response['message']['content'])