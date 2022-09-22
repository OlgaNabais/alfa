from django.urls import path
from .views import AnimalCreateView, home, about

app_name = 'animal'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('novo/', AnimalCreateView.as_view(), name='novo')
]