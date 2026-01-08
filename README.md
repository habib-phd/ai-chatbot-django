# 🤖 AI Chatbot Django Project

![Python](https://img.shields.io/badge/python-3.10+-blue) 
![Django](https://img.shields.io/badge/django-5.x-green) 
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A simple AI-powered chatbot built using **Django** and **OpenAI API**. This project provides a REST API endpoint to send messages and receive AI-generated responses. Perfect for integrating into web or mobile applications.

---

## 🚀 Project Overview

This AI Chatbot Django project is designed to demonstrate:

- How to build a RESTful API using **Django REST Framework**.
- Integration with **OpenAI GPT models**.
- Easy setup and deployment locally or on the cloud.
- JSON-based POST requests for AI interaction.

**Features:**

- REST API endpoint for sending messages.
- AI-generated responses using OpenAI GPT.
- Lightweight, modular, and easy-to-extend Django project.
- Ready for testing, development, and production environments.

---

## 🛠 Tech Stack

- **Backend:** Django 5.x, Django REST Framework  
- **AI Service:** OpenAI API  
- **Database:** SQLite (default; easy to switch to PostgreSQL/MySQL)  
- **Python Version:** 3.10+  
- **Environment Management:** Conda or virtualenv  

---

## 📦 Installation

1. **Clone the repository:**

```bash
# 1. Clone the repository
git clone https://github.com/habib-phd/ai-chatbot-django.git
cd ai-chatbot-django

# 2. Create and activate a Conda virtual environment
conda create -n ai-chatbot python=3.10 -y
conda activate ai-chatbot

# 3. Install required packages
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Start the Django development server
python manage.py runserver

# 6. (Optional) Set your OpenAI API key in the terminal
export OPENAI_API_KEY="your_openai_api_key"

