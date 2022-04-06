from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class QuestionDetailView(APIView):
    """ Вывод тестов """
    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)


class AnswerDetailView(APIView):
    def get(self, request):
        answer = Answer.objects.all()
        serializer = AnswerSerializer(answer, many=True)
        return Response(serializer.data)