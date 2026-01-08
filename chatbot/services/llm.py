import os
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)
from django.conf import settings


def get_ai_response(message: str) -> str:
    """
    Send a message to OpenAI GPT and return the response.
    """
    if not message:
        return "Please provide a message."

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": message},
        ],
        max_tokens=150)
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
