import base64
from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from google.cloud import speech

VOICEFLOW_API = ''  # Voiceflow API 키 넣기

def index(request):
    user_id = 'unique_user_id'  # 사용자 고유 ID 설정
    initial_message = get_initial_message(user_id)
    return render(request, 'chatbot/index.html', {'initial_message': initial_message})

def speech_page(request):
    user_id = 'unique_user_id'  # 사용자 고유 ID 설정
    initial_message = get_initial_message(user_id)
    return render(request, 'chatbot/speech.html', {'initial_message': initial_message})

def get_initial_message(user_id):
    url = f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact?logs=off"
    payload = {
        "action": {"type": "launch"},
        "config": {
            "tts": False,
            "stripSSML": True,
            "stopAll": True,
            "excludeTypes": ["block", "debug", "flow"]
        },
        "state": {"variables": {"x_var": 2}}
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": VOICEFLOW_API
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            if 'message' in item['payload']:
                return item['payload']['message']
    return None

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        message = request.POST.get('message')
        user_id = 'unique_user_id'
        url = f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact?logs=off"
        payload = {
            "action": {"type": "text", "payload": message},
            "config": {
                "tts": False,
                "stripSSML": True,
                "stopAll": True,
                "excludeTypes": ["block", "debug", "flow"]
            },
            "state": {"variables": {"x_var": "hello"}}
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": VOICEFLOW_API
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            try:
                data = response.json()
                messages = []
                for item in data:
                    if item['type'] == 'text' and 'message' in item['payload']:
                        message = item['payload']['message']
                        delay = item['payload'].get('delay', 0)
                        messages.append({'type': 'text', 'content': message, 'delay': delay})
                    elif item['type'] == 'visual' and 'image' in item['payload']:
                        image = item['payload']['image']
                        messages.append({'type': 'image', 'content': image, 'delay': 0})
                return JsonResponse({'messages': messages})
            except ValueError as e:
                return JsonResponse({'error': 'Invalid JSON response from API'}, status=500)
        else:
            return JsonResponse({'error': 'Failed to interact with Voiceflow API'}, status=response.status_code)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
@csrf_exempt
def transcribe(request):
    if request.method == 'POST':
        audio_data = request.POST.get('audio_data')
        if not audio_data:
            return JsonResponse({'error': 'audio_data is missing'}, status=400)

        audio_content = base64.b64decode(audio_data.split(',')[1])
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(content=audio_content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
            sample_rate_hertz=48000,
            language_code="ko-KR"
        )
        try:
            response = client.recognize(config=config, audio=audio)
            transcript = ""
            for result in response.results:
                transcript += result.alternatives[0].transcript
            return JsonResponse({'transcript': transcript})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        user_id = 'unique_user_id'
        initial_message = get_initial_message(user_id)
        return render(request, 'chatbot/speech.html', {'initial_message': initial_message})