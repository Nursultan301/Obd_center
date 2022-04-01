from django.db import models


class Tickets(models.Model):
    """ Билеты """
    title = models.CharField(max_length=200, verbose_name='Билеты')

    class Meta:
        verbose_name = 'Билеты'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return self.title


class Announcements(models.Model):
    """ Объявления """

    class Meta:
        verbose_name = "Объявления"
        verbose_name_plural = "Объявления"

    description = models.TextField("Объявления", max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.description


class Feedback(models.Model):
    """ Обратная связь """

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    name = models.CharField("Имя", max_length=20)
    phone = models.CharField("Телефон", max_length=25)

    def __str__(self):
        return self.name


class Question(models.Model):
    """Вопрос"""
    tickets = models.ForeignKey(Tickets, on_delete=models.CASCADE, verbose_name='Билеты')
    text = models.TextField(verbose_name='Текст вопроса')
    image = models.ImageField(upload_to='Obd_photo/', blank=True, null=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Answer(models.Model):
    """Ответ"""
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField('Текст', max_length=255)
    right = models.BooleanField('Правильно')

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.text
