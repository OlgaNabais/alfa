from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Pessoa

# Create your views here.
#apresentação de página estática

def contacts(request):
    return render(request, 'pessoa/contacts.html')

class PessoaCreateView(CreateView):
    model = Pessoa
    fields = '__all__'
    success_url = reverse_lazy('animal:home')