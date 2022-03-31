from django.db import models


class Announcements(models.Model):
    """ Объявления """
    description = models.TextField("Объявления", max_length=255)
    active = models.BooleanField(default=True)


class Feedback(models.Model):
    """ Обратная связь """
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=25)
