from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import auth
from .models import User

# Create your views here.

def signup(request):
    if request.method == "POST":
        try:
            user = User.objects.create_user(
                user_id=request.POST['userid'],
                name=request.POST['name'],
                password=request.POST['password1']
            )
            # 회원가입 후 로그인을 바로 시키지 않음 (관리자 승인이 필요함)
            return redirect('accounts:login')
        except IntegrityError:
            # 중복된 user_id가 있는 경우 오류 메시지 표시
            return render(request, 'signup.html', {
                'error': 'This user ID is already taken. Please choose a different one.'
            })
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        userid = request.POST['userid']
        password = request.POST['password']
        user = auth.authenticate(request, user_id=userid, password=password)
        if user is not None:
            if user.is_approved in [1, 2]:  # 관리자의 승인이 필요
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': '관리자의 승인이 필요합니다. 기다려주세요.'})
        else:
            return render(request, 'login.html', {'error': 'ID 또는 비밀번호가 틀렸습니다.'})
    return render(request, 'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request,'login.html')