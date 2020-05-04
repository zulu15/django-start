#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from boards.models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def index(request):
    ultimas_preguntas = Question.objects.order_by('-pub_date')[:5]
    context = {
        'ultimas_preguntas_list': ultimas_preguntas,
    }
    return render(request,'boards/index.html',context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,"boards/detail.html",{"question":question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,"boards/results.html",{"question":question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'boards/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        
    return HttpResponseRedirect(reverse('results', args=(question.id,)))  



			
			