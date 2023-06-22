from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index_1(request):
    return HttpResponse("index_1")

def users(request):
    # users_list = User.objects.all()
    users_list = ['user1', 'user2']
    notes_list = ['notes1', 'notes2']
    context = {'users': users_list, 'notes': notes_list}
    return render(request, 'app_1/index.html', context)

def quetions(request):
    # questions_list = Question.objects.all()
    # context = {'questions_list': questions_list}
    # return render(request, 'app_1/questions.html', context)

    questions_list = Question.objects.filter(question_text__endswith="new?")
    context = {'keys_list': questions_list}
    return render(request, 'app_1/questions.html', context)