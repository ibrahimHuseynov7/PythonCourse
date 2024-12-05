from django.urls import path
from .views import index,about

urlpatterns = [
    path('', index, name='index'),
    path('us',about,name='about')
]
