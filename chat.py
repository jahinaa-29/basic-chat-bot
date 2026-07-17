import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Start a chat session 
chat = client.chats.create(model="gemini-2.0-flash")

print("Chatbot is ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit": # lowercases the input to make it case-insensitive
        print("Bot: Bye! 👋")
        break

    response = chat.send_message(user_input)
    print(f"Bot: {response.text}\n")