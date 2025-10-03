from django.shortcuts import render

# Create your views here.

def toonHTML(request):
    return render(request, 'start.html')