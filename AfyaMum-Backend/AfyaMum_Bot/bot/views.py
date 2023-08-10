from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from Llama.model import final_result
# Create your views here.

@api_view(['POST'])
def prompt(request):
    prompt = request.data.get("prompt")
    result = final_result(prompt)
    return Response(result)
