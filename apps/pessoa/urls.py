from django.urls import path
from .views import contacts, PessoaCreateView, PessoaListView, PessoaDetailView

app_name = 'pessoa'

urlpatterns = [
     path('', contacts, name='contacts'),
     path('novo/', PessoaCreateView.as_view(), name='novo'),
     path('lista/', PessoaListView.as_view(), name='lista'),
     path('detalhe/<int:pk>/', PessoaDetailView.as_view(), name='detalhe')
]
    