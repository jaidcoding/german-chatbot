# 🇩🇪 Hanz — German Language Tutor

A conversational German language learning chatbot built with Python and Flask. 
Practice your German with Hanz, an AI tutor that corrects your mistakes, 
responds naturally, and even speaks back to you in German.

## Features
- 💬 Conversational German practice with AI
- 📝 Grammar and spelling correction mode (toggle on/off)
- 🔊 Call mode — Hanz speaks his responses out loud
- 🧠 Chat history within each session
- 🌙 Clean dark mode UI
- 🆕 New chat button to reset the conversation

## Tech Stack
- Python
- Flask
- Ollama + LLaMA3 (runs locally, completely free)
- Piper TTS (local text to speech, no API needed)

## Requirements
- Python 3
- [Ollama](https://ollama.com) 
- [Piper TTS](https://github.com/rhasspy/piper)
- LLaMA3 model
- Thorsten German voice for Piper

## Setup

1. Clone the repo
   git clone https://github.com/jaidcoding/german-chatbot.git
   cd german-chatbot

2. Create and activate a virtual environment
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install flask ollama piper-tts pathvalidate

4. Install Ollama and pull LLaMA3
   ollama pull llama3

5. Download the German voice for Piper
   mkdir ~/piper-voices
   cd ~/piper-voices
   curl -L -o de_DE-thorsten-medium.onnx https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/thorsten/medium/de_DE-thorsten-medium.onnx
   curl -L -o de_DE-thorsten-medium.onnx.json https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/thorsten/medium/de_DE-thorsten-medium.onnx.json

6. Run the app
   python3 app.py

7. Open your browser and go to
   http://localhost:5000

## Notes
- Ollama and Piper run completely locally — no API keys or costs ever
- Chat history resets when you restart the server
- Tested on macOS with M1