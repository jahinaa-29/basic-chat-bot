# Basic Chat Bot

A simple terminal-based chatbot powered by Google's Gemini API. Type a message, get a response, and keep the conversation going — built as a first hands-on AI project.

## Description

This project is a command-line chatbot that connects to Google's Gemini API to have real-time, back-and-forth conversations. It uses the `google-genai` Python SDK to send user input to the Gemini model and print back its responses, while maintaining conversation history so the bot remembers earlier context in the same session. API keys are kept secure using a `.env` file, which is excluded from version control via `.gitignore`. This project was built as an introduction to working with LLM APIs, environment variables, and basic Python project structure.

## Getting Started

### Dependencies

* Python 3.13 (or 3.9+)
* macOS, Windows, or Linux
* A free [Google AI Studio](https://aistudio.google.com/apikey) account for an API key
* Libraries: `google-genai`, `python-dotenv` (installed below)

### Installing
