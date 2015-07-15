from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Question

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', {'question_list': question_list,})

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/details.html',
                      {
                          'question': question,
                          'error_message': 'No choice was selected.'
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
    return HttpResponse("You are voting on question %s." % question_id)