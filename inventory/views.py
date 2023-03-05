from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def Inventory(request):
    context = {}
    return render(request, 'inventory/main.html', context)

