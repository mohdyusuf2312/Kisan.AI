from django.urls import path
from . import views

urlpatterns = [
    path('ai/', views.chat_with_ai, name='chat_with_ai'),
    path('order/', views.order, name='order'),
]
