from django.shortcuts import render

# Create your views here.

def recommendation_home(request):
    return render(request, 'inventory_recommendation/home.html')
