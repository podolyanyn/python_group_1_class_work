from django.urls import path

from . import views
from django.http import HttpResponse




urlpatterns = [
    path('qwerty/', views.index),
    path('qwerty_1/', views.index),
    path('', views.users),
    path('quetions', views.quetions),

]