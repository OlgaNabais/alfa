from django.urls import path
from .views import contacts

app_name = 'pessoa'

urlpatterns = [
     path('', contacts, name='contacts')
]
    