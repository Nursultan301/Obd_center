from rest_framework import serializers

from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    """Список Ответов"""

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    """Список тестов"""
    answer = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ('img', 'title', 'answer')