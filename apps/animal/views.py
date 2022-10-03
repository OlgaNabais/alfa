from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Animal

# Create your views here.
#apresentação de página estática

def home(request):
    return render(request, 'animal/home.html')

def about(request):
    return render(request, 'animal/about.html')

class AnimalCreateView(CreateView):
    model = Animal
    fields = '__all__'
    success_url = reverse_lazy('animal:lista')

class AnimalListView(ListView):
    model = Animal

class AnimalDetailView(DetailView):
    model = Animal

class AnimalUpdateView(UpdateView):
    model = Animal
    fields = ['nome', 'idade']
    template_name = 'animal/animal_update.html'
    success_url = reverse_lazy('animal:lista')

class AnimalUpdateDetailView(UpdateView):
    model = Animal
    fields = ['nome', 'idade']
    template_name = 'animal/animal_detail_update.html'
   
    def get_success_url(self):
        return reverse('animal:detalhe', kwargs={'pk': self.object.id})

class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy('animal:lista')

class AnimalDeleteDetailView(DeleteView):
    model = Animal
    template_name = 'animal/animal_detail_confirm_delete.html'
    success_url = reverse_lazy('animal:lista')
