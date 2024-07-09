from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json

VOICEFLOW_API = '' #voiceflow api키 넣기 

def index(request):
    user_id = 'unique_user_id'  # 사용자 고유 ID 설정
    initial_message = get_initial_message(user_id)
    return render(request, 'chatbot/index.html', {'initial_message': initial_message})

def get_initial_message(user_id):
    # Voiceflow API에 요청하여 초기 메시지를 가져옴
    url = f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact?logs=off"

    payload = {
        "action": { "type": "launch" },
        "config": {
            "tts": False,
            "stripSSML": True,
            "stopAll": True,
            "excludeTypes": ["block", "debug", "flow"]
        },
        "state": { "variables": { "x_var": 2 } }
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": VOICEFLOW_API  # Voiceflow API 키로 교체하세요
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    
    if response.status_code == 200:
        data = response.json()
        # 응답 데이터 구조를 확인 후 message 부분 추출
        for item in data:
            if 'message' in item['payload']:
                return item['payload']['message']
    
    return None  # 실패 시 None 반환 또는 예외 처리

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        message = request.POST.get('message')
        user_id = 'unique_user_id'  # 사용자 고유 ID 설정
        print(message)
        url = f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact?logs=off"
        
        payload = {
            "action": {
                "type": "text",
                "payload": message
            },
            "config": {
                "tts": False,
                "stripSSML": True,
                "stopAll": True,
                "excludeTypes": ["block", "debug", "flow"]
            },
            "state": { "variables": { "x_var": "hello" } }
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": VOICEFLOW_API  # Voiceflow API 키로 교체하세요
        }
        
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        
        if response.status_code == 200:
            try:
                data = response.json()
                messages = []
                # Voiceflow API에서 응답으로 받은 데이터 처리
                if isinstance(data, list):
                    for item in data:
                        if 'message' in item.get('payload', {}):
                           messages.append(item['payload']['message'])
                elif isinstance(data, dict) and 'message' in data.get('payload', {}):
                    messages.append(data['payload']['message'])
                return JsonResponse({'messages': messages})
            except ValueError as e:
                return JsonResponse({'error': 'Invalid JSON response from API'}, status=500)
        else:
            return JsonResponse({'error': 'Failed to interact with Voiceflow API'}, status=response.status_code)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)  # POST 요청이 아닐 경우 에러 처리
