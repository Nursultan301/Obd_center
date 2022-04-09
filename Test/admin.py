from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Announcements, Feedback, Answer, Question, Ticket


class QuestionAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Question
        fields = '__all__'


@admin.register(Ticket)
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


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Вопрос"""
    list_display = ('title', 'img', 'ticket', 'created_at')
    inlines = [AnswerInline]