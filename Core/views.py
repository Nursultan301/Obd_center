from django.shortcuts import render
from django.views.generic import ListView

from .models import Announcements, Question, Answer


class AnnouncementsView(ListView):
    model = Announcements
    template_name = 'Core/index.html'
    context_object_name = 'objs'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(AnnouncementsView, self).get_context_data(**kwargs)
        context['tests'] = Question.objects.all()
        context['tests1'] = Answer.objects.all()
        return context


