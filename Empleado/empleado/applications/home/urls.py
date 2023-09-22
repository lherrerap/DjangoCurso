from django.urls import path
from .views import *

urlpatterns = [
    path('home/', IndexView.as_view()),
    path('lista/', PruebaView.as_view()),
    path('lista_prueba/', PruebaListView.as_view())
]
