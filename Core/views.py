from django.shortcuts import render
from django.views.generic import ListView

from .models import Announcements, Question, Answer


class AnnouncementsView(ListView):
    model = Announcements
    template_name = 'Core/index.html'
    context_object_name = 'obj'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AnnouncementsView, self).get_context_data(**kwargs)
        context['test'] = Question.objects.all()
        context['test1'] = Answer.objects.all()
        return context


