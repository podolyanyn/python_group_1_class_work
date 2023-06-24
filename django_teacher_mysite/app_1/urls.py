from django.urls import path

from . import views
from django.http import HttpResponse

app_name = "app_1"
urlpatterns = [
    # path('qwerty/', views.index),
    # path('qwerty_1/', views.index),
    # path('', views.users),
    # path('quetions', views.quetions),
    # # ex: /polls/
    # path("", views.index, name="index"),
    # # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),

    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("new_question/", views.new_question, name="new_question"),
    path("new_question_thanks/", views.new_question_thanks, name="new_question_thanks"),
]