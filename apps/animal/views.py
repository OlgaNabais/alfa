from django.shortcuts import render

# Create your views here.
#apresentação de página estática

def home(request):
    return render(request, 'animal/home.html')

def about(request):
    return render(request, 'animal/about.html')