from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.llm import get_ai_response

@api_view(['POST'])
def chat(request):
    user_message = request.data.get("message", "")
    reply = get_ai_response(user_message)
    return Response({"reply": reply})
