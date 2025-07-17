from django.urls import path
from . import views

urlpatterns = [
    path('', views.analysis_home, name='analysis_home'),
]
