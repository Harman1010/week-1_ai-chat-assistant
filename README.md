# AI Chat Assistant

An AI-powered chatbot built with **Python**, supporting both a **Command Line Interface (CLI)** and a **REST API** using **FastAPI**. The application integrates with a Large Language Model (LLM) to answer user queries, making it easy to interact with AI from the terminal or through HTTP requests.

## Features

* AI-powered conversational assistant
* Interactive Command Line Interface (CLI)
* REST API built with FastAPI
* Interactive API documentation with Swagger UI
* Environment variable support using `.env`
* Modular and maintainable project structure
* Reusable AI logic shared between the CLI and API

---

## Project Structure

```text
AI-Chat-Assistant/
│
├── app/
│   ├── app.py            # FastAPI application
│   ├── chat.py           # CLI chat loop
│   ├── llm.py            # AI model integration
│   ├── routes.py         # API endpoints
│   ├── schemas.py        # Request and response models
│   ├── config.py         # Configuration
│   └── __init__.py
│
├── main.py               # CLI entry point
├── requirements.txt
├── .env
├── .env.example
└── README.md
```

---

## Tech Stack

### Language

* Python 3.11+

### Frameworks & Libraries

* FastAPI
* Uvicorn
* Pydantic
* python-dotenv
* Google Gemini API (or your configured LLM)

---

## Installation

### 1. Clone the repository

```powershell
git clone <https://github.com/Harman1010/week-1_ai-chat-assistant.git>
cd AI-Chat-Assistant
```

### 2. Create a virtual environment

Windows

```powershell
python -m venv venv
venv\Scripts\activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file by copying `.env.example`.

Then update the API key with your own credentials.

---

# Running the CLI

Start the chatbot using:

```bash
python main.py
```

Example:

```text
Welcome, I'm your AI Chat Assistant
Type 'exit' to finish the session.

User: What is AI?

AI:
Artificial Intelligence is the simulation of human intelligence by machines...

User: exit

Thank you for your time!
```

---

# Running the FastAPI Server

Start the API server:

```bash
uvicorn app.app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

**GET /**

Response

```json
{
    "status": "running"
}
```

### Chat Endpoint

**POST /chat**

Request

```json
{
    "message": "What is Artificial Intelligence?"
}
```

Response

```json
{
    "message": "Artificial Intelligence (AI) is..."
}
```

---

## How It Works

1. The user sends a prompt through either the CLI or the REST API.
2. The request is forwarded to the shared AI service.
3. The LLM processes the prompt.
4. The generated response is returned to the user.
5. Both interfaces reuse the same AI logic, avoiding code duplication.

---

## Future Improvements

* Conversation history
* Streaming AI responses
* Authentication
* Multiple LLM providers
* Web frontend (HTML/CSS/JavaScript or React)
* Persistent chat storage
* Docker support
* Unit and integration tests

---
