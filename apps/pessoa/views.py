from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Pessoa

# Create your views here.
#apresentação de página estática

def contacts(request):
    return render(request, 'pessoa/contacts.html')

class PessoaCreateView(CreateView):
    model = Pessoa
    fields = '__all__'
    success_url = reverse_lazy('pessoa:lista')

class PessoaListView(ListView):
    model = Pessoa

class PessoaDetailView(DetailView):
    model = Pessoa