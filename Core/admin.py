from django.contrib import admin

from .models import Announcements, Feedback, Answer, Question, Tickets


@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    """ Билеты """
    pass


@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    """ Объявления """
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """ Обратная связь """
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Ответ"""

    list_display = ('text', 'right', 'question')


class QuestionsInline(admin.TabularInline):
    model = Answer
    extra = 1


@admin.register(Question)
class BookAdmin(admin.ModelAdmin):
    """Вопрос"""
    list_display = ('text', 'image', 'tickets', 'created_at')
    inlines = [QuestionsInline]
