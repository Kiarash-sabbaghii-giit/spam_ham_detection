# detector/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('history/', views.history_view, name='history'),
    path('predict/', views.predict, name='predict'),
    path('clear-history/', views.clear_history, name='clear_history'),
]