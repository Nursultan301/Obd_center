from rest_framework import serializers

from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    """Список тестов"""

    class Meta:
        model = Question
        fields = ('img', 'title')


class AnswerSerializer(serializers.ModelSerializer):
    """Список тестов"""

    class Meta:
        model = Answer
        fields = '__all__'
