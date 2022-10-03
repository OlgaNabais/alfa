from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
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

class PessoaUpdateView(UpdateView):
    model = Pessoa
    fields = ['nome', 'idade', 'email']
    template_name = 'pessoa/pessoa_update.html'
    success_url = reverse_lazy('pessoa:lista')

class PessoaUpdateDetailView(UpdateView):
    model = Pessoa
    fields = ['nome', 'idade', 'email']
    template_name = 'pessoa/pessoa_detail_update.html'
    
    def get_success_url(self):
        return reverse('pessoa:detalhe-atualizar',kwargs={'pk': self.object.id})

class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url: reverse_lazy('pessoa:lista')

class PessoaDeleteDetailView(DeleteView):
    model = Pessoa
    template_name = 'pessoa/pessoa_detail_confirm_delete.html' 
    success_url = reverse_lazy('pessoa:lista')
