from django.urls import path

from .views import QuestionDetailView, AnswerDetailView

urlpatterns = [
    path('test/', QuestionDetailView.as_view()),
    path('question/', AnswerDetailView.as_view())
]