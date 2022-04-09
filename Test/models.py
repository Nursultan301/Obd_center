import os

from django.db import models
from django.urls import reverse


class Announcements(models.Model):
    """ Объявления """

    description = models.TextField("Объявления", max_length=255)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Объявления"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.description


class Feedback(models.Model):
    """ Обратная связь """

    name = models.CharField("Имя", max_length=20)
    phone = models.CharField("Телефон", max_length=25)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return self.name


class Ticket(models.Model):
    """ Билеты """
    title = models.CharField(max_length=200, verbose_name='Билеты')

    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"pk": self.pk})
    
    def get_json_url(self):
        return reverse("ticket_json", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Билеты'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return self.title


class Question(models.Model):
    """Вопрос"""
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name='Билеты')
    img = models.ImageField(upload_to='Obd_photo/', blank=True, null=True)
    title = models.TextField(verbose_name='Текст вопроса')
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def filename(self):
        return os.path.basename(self.img.name)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title


class Answer(models.Model):
    """Ответ"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопросы")
    answer = models.CharField('Вопросы', max_length=255)
    correctAnswer = models.BooleanField('Правильно')

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.answer
