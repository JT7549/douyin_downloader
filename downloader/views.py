#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from.models import UserInfo
#import requests
import os
from django.http import HttpResponse, JsonResponse
import re

# 视图函数处理GET请求
def download(request):
    url = request.GET.get('url')  # 获取GET请求中的url参数
    if not url:
        return JsonResponse({'error': 'URL parameter is missing'}, status=400)

    # 解析抖音视频链接
    try:
        # 示例解析逻辑，实际需要根据抖音API调整
        response = request.get(url)
        video_url = re.search(r'video_url_pattern', response.text).group(1)
        return JsonResponse({'video_url': video_url})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def home(request):
    return render(request, 'home.html')

#def download(request):
    if request.method == 'GET':
        url = request.GET.get('url')
        # 使用第三方库或自定义逻辑解析抖音视频链接
         #示例：使用requests获取视频数据
        response = request.get(url)
        if response.status_code == 200:
            video_data = response.content
            return HttpResponse(video_data, content_type='video/mp4')
        else:
            return HttpResponse("Failed to download video", status=400)
    return render(request, 'download.html')
    



def insert_data(request):
    data_list = [
        {'id': 1, 'name': 'John', 'age': 25},
        {'id': 2, 'name': 'Alice', 'age': 30}
    ]
    for data in data_list:
        UserInfo.objects.create(
            id=data['id'],
            name=data['name'],
            age=data['age']
        )
    return HttpResponse("Data inserted successfully")



#def download(request):
    # 假设请求中有一个名为 'url' 的参数，从中获取实际的视频URL
    video_url = request.GET.get('url')
    if video_url:
        try:
            response = request.get(video_url)
            file_name = os.path.basename(video_url)
            with open(file_name, 'wb') as f:
                f.write(response.content)
            # 处理下载逻辑，例如保存文件等
            #...
            return HttpResponse("下载成功")
        except request.RequestException as e:
            return HttpResponse(f"下载失败: {str(e)}")
    else:
        return HttpResponse("缺少视频URL参数")
    
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from.forms import CustomUserCreationForm

def register(request):
    if request.method == 'GET':
        form = CustomUserCreationForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request,'register.html', {'form': form})

def user_login(request):
    if request.method == 'GET':
        form = AuthenticationForm(request, data=request.GET)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # 替换为实际主页URL名称
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')    

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def protected_view(request):
    return render(request, 'protected.html')