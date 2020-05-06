#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date <= timezone.now()  - datetime.timedelta(days=1)

    def total_votes(self):
        return sum(p.votes for p in self.choice_set.all())

        

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #random = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    def votes_as_percentage(self):
        return "{:.2f}".format((self.votes / self.question.total_votes()) * 100) if self.votes else 0;



