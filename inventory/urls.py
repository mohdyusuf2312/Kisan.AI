from django.urls import path
from . import views

urlpatterns = [
    path('', views.season, name='home'),
    path('season/', views.season, name='season'),
    path('crops/', views.crops, name='crops'),
    path('fertilizer/', views.fertilizer, name='fertilizer'),
    path('seed/', views.seed, name='seed'),
    path('profit/', views.profit, name='profit'),
    path('utilized/', views.utilized, name='utilized'),
    path('table/', views.table, name='table'),
]
