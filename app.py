from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)
conversation_history = []
corrections_on = True

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global corrections_on
    user_input = request.json.get("message")

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    if corrections_on:
        system = "You are Hanz, a friendly German tutor helping a beginner practice conversational German. Even if their German is broken or mixed with English, try your best to understand what they mean and respond naturally. Respond in simple German with an English translation in parentheses after each sentence. ONLY respond to what the user said. Ask ONE follow up question maximum. Never simulate a full conversation or speak for the user. Keep your response to 2 sentences max. IMPORTANT: You must ALWAYS check if the user wrote any German. If they did, you MUST look for any spelling, grammar, or vocabulary mistakes no matter how small. Always add a correction section starting with '📝 Hanz says:' even if the only mistake is a missing accent or a small grammar error. If their German is perfect, say '📝 Hanz says: Perfekt! No mistakes this time.'"
    else:
        system = "You are Hanz, a friendly German tutor helping a beginner practice conversational German. Even if their German is broken or mixed with English, try your best to understand what they mean and respond naturally. Respond in simple German with an English translation in parentheses after each sentence. ONLY respond to what the user said. Ask ONE follow up question maximum. Never simulate a full conversation or speak for the user. Keep your response to 2 sentences max."

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": system
            }
        ] + conversation_history
    )

    assistant_message = response['message']['content']

    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return jsonify({"response": assistant_message})
    
    assistant_message = response['message']['content']
    
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return jsonify({"response": assistant_message})

@app.route("/toggle-corrections", methods=["POST"])
def toggle_corrections():
    global corrections_on
    corrections_on = request.json.get("corrections")
    return jsonify({"status": "ok"})

@app.route("/clear-chat", methods=["POST"])
def clear_chat():
    global conversation_history
    conversation_history = []
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)