from django.urls import path 
from .views import *

urlpatterns = [ 
    path('', index, name='index'),
    path('add_item/', add_item),
]