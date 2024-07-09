from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .km_bert_model import specialty_predict

@csrf_exempt
def get_recommendation(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            user_symptom = body.get('symptom')
            if not user_symptom:
                return JsonResponse({'error': 'No symptom provided'}, status=400)

            departments, probs = specialty_predict(user_symptom)
            response = {
                'recommended_departments': departments.split(', '),
                'probabilities': probs.tolist()
            }
            return JsonResponse(response)
        except Exception as e:
            import traceback
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

