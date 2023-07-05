import time

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Question, Choice
from django.contrib.auth.models import User
from django.http import Http404
from django.urls import reverse
from django.views import generic
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import asyncio, httpx
from asgiref.sync import sync_to_async



# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "app_1/index.html", context)

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "app_1/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(user=self.request.user).order_by("-pub_date")[:5]




# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "app_1/detail.html", {"question": question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "app_1/results.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "app_1/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "app_1/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "app_1/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("app_1:results", args=(question.id,)))




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

@login_required
def new_question(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            q = Question(question_text=form.cleaned_data['question_text'],
                         pub_date=form.cleaned_data['pub_date'],
                         user=form.cleaned_data['user'])
            q.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("app_1:new_question_thanks"))
            # return HttpResponseRedirect('/app_1/new_question_thanks/')
            # return HttpResponse('New question is created !')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    return render(request, 'app_1/new_question.html', {'form': form})

def new_question_thanks(request):
    return HttpResponse('New question is created !')


def index_1(request):
    # return HttpResponse("this is index_1")
    time.sleep(1)
    return JsonResponse({'result_json':"this is index_1", 'test':'test1'})

# ----------- async
async def index_1_async(request):
    # return HttpResponse("this is index_1")
    await asyncio.sleep(1)
    return JsonResponse({'result_json':"this is index_1", 'test':'test1'})

@sync_to_async
def index_async(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


async def async_index(request):
    return HttpResponse("Hello, async Django!")


# async def http_call_async():
#     for num in range(1, 6):
#         await asyncio.sleep(1)
#         print(num)
#     async with httpx.AsyncClient() as client:
#         r = await client.get("https://httpbin.org/")
#         print(r)


async def async_view(request):
    # loop = asyncio.get_event_loop()
    # loop.create_task(http_call_async())
    for num in range(1, 4):
        await asyncio.sleep(1)
        print(num)
    return HttpResponse("Non-blocking HTTP request")

