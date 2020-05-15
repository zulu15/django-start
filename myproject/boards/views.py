#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from boards.models import Question, Choice, Vote, Comentario
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from boards.forms import PollForm, ChoiceForm, ComentarioForm
from django.utils import timezone
from django.forms import formset_factory
from django.contrib import messages





class IndexView(generic.ListView):
    template_name = 'boards/index.html'
    context_object_name = 'ultimas_preguntas_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]



def create_poll(request):

    ChoiceFormSet = formset_factory(ChoiceForm, extra=2)

    if request.method == 'POST':

        pollForm = PollForm(request.POST, request.FILES)
        formset = ChoiceFormSet(request.POST, request.FILES)

        if pollForm.is_valid() and formset.is_valid():
            question = pollForm.save(commit=False) 
            user =  request.user
            if user is not None:
                question.author = user
                question.pub_date = timezone.now()
                question.save()  
                for form in formset.forms:
                    choice = form.save(commit=False)
                    if len(choice.choice_text) > 0:   
                        question.choice_set.create(choice_text=choice.choice_text)
        
        messages.success(request, 'Se añadió tu pregunta correctamente!')    
        return HttpResponseRedirect(reverse('index'))  
    else:
        pollForm = PollForm()   
        choiceFormSet = ChoiceFormSet()
        return render(request, 'boards/create_poll.html', {'pollForm':pollForm, 'formset': ChoiceFormSet})

            






class DeletePollView(generic.DeleteView):
    model = Question
    #template_name = 'boards/poll_confirm_delete.html'
    #success_url = reverse('index')

    def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       if self.object.author == request.user:
          self.object.delete()
          messages.success(request, 'Se eliminó la pregunta correctamente!.')
          return HttpResponseRedirect(self.get_success_url())
       else:
            messages.warning(request, 'No puedes eliminar una pregunta que no es de tu autoria!.')
            return HttpResponseRedirect(reverse('index'))  

    def get_success_url(self):
        return reverse('index')



class DetailView(generic.DetailView):
    model = Question
    template_name = 'boards/results.html'
    form_class = ComentarioForm


   

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        return context;    

    def post(self, request, *args, **kwargs ):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            c = form.save(commit = False)
            c.usuario = request.user
            c.question = Question.objects.get(pk=kwargs.get('pk'))
            c.save()
            return HttpResponseRedirect(reverse_lazy('detail', kwargs = {'pk': kwargs.get('pk')}))

def vote(request, question_id):

    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        try:
            #Chequeamos que el usuario no haya votado a esta pregunta
            if Vote.objects.filter(choice__question__id = question_id, usuario__id = request.user.id).count() > 0:
                messages.warning(request, 'Ya has votado esta pregunta, solo se permite un voto por pregunta!.')
                return HttpResponseRedirect(reverse('index'))  

            selected_choice = question.choice_set.get(pk=request.POST['choice'])
            selected_choice.vote_set.create(usuario=request.user)
            messages.success(request, 'Tu voto fue añadido correctamente!.')
            return HttpResponseRedirect(reverse('index'))  
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            #request.session['error'] = "Debes seleccionar una opción!"
            messages.warning(request, 'No se ha encontrado la opcion indicada, vuelve a intentarlo!.')
            return HttpResponseRedirect(reverse('index'))  
    else:

        question = Question.objects.get(pk = question_id)
        return render(request, 'boards/detail.html', {'question': question})
