import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST request required"},
            status=400
        )

    try:
        data = json.loads(request.body)
        user_message = data.get("message")

        if not user_message:
            return JsonResponse(
                {"error": "Message is required"},
                status=400
            )

        # TEMP response (AI comes next)
        return JsonResponse({
            "user": user_message,
            "bot": f"You said: {user_message}"
        })

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )
