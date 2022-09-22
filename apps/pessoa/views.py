from django.shortcuts import render

# Create your views here.
#apresentação de página estática

def contacts(request):
    return render(request, 'pessoa/contacts.html')

