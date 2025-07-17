from django.urls import path
from . import views

urlpatterns = [
    path('', views.yolo_home, name='yolo_home'),
]
