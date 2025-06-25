# 🧠 AI Chatbot Dashboard

An advanced AI chatbot web application built with **Django**. This project enables user authentication, chat session tracking, and seamless interaction with an AI assistant (like OpenAI’s GPT models). Ideal for educational, business, or personal virtual assistant use cases.

---

## 🔧 Features

- ✅ User registration and login
- ✅ Chat interface with AI assistant
- ✅ Session-based chat history
- ✅ Admin panel for user management
- ✅ Responsive UI with Bootstrap
- ✅ MongoDB or PostgreSQL database support
- ✅ Ready for production deployment on Railway

---

## 📸 Demo

![AI Chatbot Dashboard](docs/demo.gif) <!-- Optional: Add a GIF or screenshot of chat -->

---

## 🗂️ Tech Stack

| Layer        | Technology              |
|--------------|-------------------------|
| Framework    | Django                  |
| Frontend     | HTML5, CSS3, Bootstrap  |
| Backend AI   | OpenAI API (ChatGPT)    |
| Database     | PostgreSQL / MongoDB    |
| Deployment   | Railway (or Render)     |

---


## 🚀 Getting Started

### 1. Clone the repo

bash
git clone https://github.com/your-username/ai-chatbot-dashboard.git
cd ai-chatbot-dashboard

### 2. Create a virtual environment and activate it

python -m venv venv

source venv/bin/activate   # For Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Set environment variables
Create a .env file in the root:

OPENAI_API_KEY=your_openai_api_key

SECRET_KEY=your_django_secret_key

DEBUG=True

🔐 Don't forget to set DEBUG=False in production.

### 5. Run migrations and start the server

python manage.py migrate

python manage.py runserver

Visit: http://127.0.0.1:8000

---

## 💬 How It Works

Users can register and start chatting with the AI.

Chat sessions are tracked per user.

You can plug in any AI backend (e.g., OpenAI, Claude, etc.).

---

## ⚙️ Deployment (Railway)
Push to a GitHub repository.

Connect your GitHub repo to Railway.

Add environment variables: OPENAI_API_KEY, DEBUG, SECRET_KEY.

Set up PostgreSQL/MongoDB plugin.

Use the following build and start commands:

Build: pip install -r requirements.txt
Start: gunicorn ai_chatbot_dashboard.wsgi:application

---

## 🧪 Example .env for Railway

OPENAI_API_KEY=sk-xxxxx

SECRET_KEY=your_production_secret_key

DEBUG=False

DATABASE_URL=postgres://user:pass@host:port/dbname

---

## 📄 License
MIT License. Feel free to use and modify it for your own projects.

---

## Author
Nithin P
nithinpsea10@gmail.com

---
