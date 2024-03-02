import os
import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def classifyText(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text')
        try:
            print(f'text:',text)
        except:
            return JsonResponse({"error": "no response"}, status=400)
        return JsonResponse({"message": "response returned successfully", "text": text})