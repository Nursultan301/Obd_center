from django.db import models


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