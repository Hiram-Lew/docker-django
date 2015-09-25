from django.shortcuts import render
from django.http import HttpResponse
from .secure import secure_required 
# Create your views here.

@secure_required
def index(request):
    return HttpResponse("Hello word. You're in the messages index")

