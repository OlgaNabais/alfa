from django.urls import path
from .views import contacts, PessoaCreateView

app_name = 'pessoa'

urlpatterns = [
     path('', contacts, name='contacts'),
     path('novo/', PessoaCreateView.as_view(), name='novo')
]
    