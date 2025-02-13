from django.shortcuts import render
from .models import Project
from django.http import HttpResponse
import os
from django.conf import settings
# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def debug_media(request):
    media_files = []
    import sys
    print(f"Python path: {sys.path}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
    print(f"Directory exists: {os.path.exists(settings.MEDIA_ROOT)}")
    for root, dirs, files in os.walk(settings.MEDIA_ROOT):
        print(f"Checking directory: {root}")
        print(f"Found files: {files}")
        for file in files:
            media_files.append(os.path.join(root, file))
    return HttpResponse(f"""
        MEDIA_ROOT: {settings.MEDIA_ROOT}<br>
        Directory exists: {os.path.exists(settings.MEDIA_ROOT)}<br>
        Files found:<br>{'<br>'.join(media_files)}
    """)