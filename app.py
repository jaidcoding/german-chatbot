from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)
conversation_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": "You are a friendly German tutor who understands that the user is a beginner. Even if their German is broken or mixed with English, try your best to understand what they mean and respond naturally. Respond in simple German with an English translation in parentheses after each sentence. ONLY respond to what the user said. Ask ONE follow up question maximum. Never simulate a full conversation or speak for the user. Keep it to 2 sentences max."
            }
        ] + conversation_history
    )
    
    assistant_message = response['message']['content']
    
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return jsonify({"response": assistant_message})

if __name__ == "__main__":
    app.run(debug=True)