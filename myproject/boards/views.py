#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from boards.models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from boards.forms import PollForm, ChoiceForm
from django.utils import timezone
from django.forms import formset_factory

class IndexView(generic.ListView):
    template_name = 'boards/index.html'
    context_object_name = 'ultimas_preguntas_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]



def create_poll(request):
    ChoiceFormSet = formset_factory(ChoiceForm, extra=2)

    if request.method == 'POST':

        pollForm = PollForm(request.POST)
        formset = ChoiceFormSet(request.POST, request.FILES)

        if pollForm.is_valid() and formset.is_valid():
            question = pollForm.save(commit=False) 
            question.pub_date = timezone.now()
            question.save()  
            for form in formset.forms:
                choice = form.save(commit=False)
                question.choice_set.create(choice_text=choice.choice_text, votes=0)
        return HttpResponseRedirect(reverse('index'))  
    else:
        pollForm = PollForm()   
        choiceFormSet = ChoiceFormSet()
        return render(request, 'boards/create_poll.html', {'pollForm':pollForm, 'formset': ChoiceFormSet})

            


class DetailView(generic.DetailView):
    model = Question
    template_name = 'boards/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'boards/results.html'


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
        
    return HttpResponseRedirect(reverse('results',args= (question.id,) ))  

