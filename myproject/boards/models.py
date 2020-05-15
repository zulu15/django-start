#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


# Create your models here.

class Question(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', blank=True)
    image = ImageField(blank = True  , null= True , default="none/no-img.jpeg")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date <= timezone.now()  - datetime.timedelta(days=1)

    def total_votes(self):
        return Vote.objects.filter(choice__question__id=self.id).count()

        

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE,  blank=True, null=True )
    choice_text = models.CharField(max_length=200)
    
    #random = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    def votes_as_percentage(self):
        return "{:.2f}".format((self.vote_set.all().count() / self.question.total_votes()) * 100) if self.vote_set.all().count() > 0 else 0;
      


class Vote(models.Model):
    class Meta:
        unique_together = (('choice', 'usuario'),)

    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=1, blank=True)



    def __str__(self):
        return '{} / {} / {}'.format(self.choice.question.question_text, self.choice.choice_text ,self.usuario.username)



class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now = False, auto_now_add = True)
    comentario = models.CharField(max_length=200)
    respuesta = models.ForeignKey("Comentario", null=True, blank=True,related_name="respuestas", on_delete=models.SET_NULL, default=None)

    def __str__(self):
        return self.comentario;


