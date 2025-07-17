from django.shortcuts import render

# Create your views here.

def yolo_home(request):
    return render(request, 'yolo/home.html')
