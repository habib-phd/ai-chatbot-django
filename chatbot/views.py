from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def chat(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        # Temporary response (LLM will come later)
        response = {
            "reply": f"You said: {user_message}"
        }

        return JsonResponse(response)

    return JsonResponse({"error": "POST request required"}, status=400)

