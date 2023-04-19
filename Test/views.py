import json
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import JsonResponse, FileResponse
from django.conf import settings

from .models import Question, Answer, Ticket


class TicketDetailView(TemplateView):
    template_name = 'Test/index.html'

    def get(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        return render(request, self.template_name, {'ticket': ticket, 'get_json': str(ticket.get_json_url())})


class TicketDetailJsonView(View):
    """ Вывод тестов """
    def get(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        questions = Question.objects.all().filter(ticket=ticket)
        data = {"countQuest": questions.count(), "quests": []}
        data_list, data_dict = [],  {}
        for q in questions:
            answers, correctAnswer, answer_list = Answer.objects.filter(question=q), 0, []
            for a in answers:
                count = len(answer_list)
                answer_list.append(a.answer)
                if a.correctAnswer:
                    correctAnswer = count + 1
            data_dict = {
                "img": q.filename() if q.img else "none",
                "title": str(q.title),
                "answer": answer_list,
                "correctAnswer": correctAnswer
            }
            data_list.append(data_dict)
        data["quests"] = data_list
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
