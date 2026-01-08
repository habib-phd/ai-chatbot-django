from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from chatbot.services.llm import generate_response


@csrf_exempt
def chat(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        reply = generate_response(user_message)

        return JsonResponse({"reply": reply})

    return JsonResponse({"error": "POST request required"}, status=400)

