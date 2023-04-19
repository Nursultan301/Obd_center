from django.db import models
from common import constants as cons


class Category(models.Model):
    title = models.CharField("Название категории", max_length=3)
    price = models.PositiveSmallIntegerField("Сумма обучение", default=5000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class CategoryInfo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    info = models.CharField("Этапы", max_length=255)

    class Meta:
        verbose_name = "Этап"
        verbose_name_plural = "Этапы"


class Discount(models.Model):
    PRICE = [
        (cons.PRICE_250, cons.PRICE_250),
        (cons.PRICE_500, cons.PRICE_500),
        (cons.PRICE_1000, cons.PRICE_1000),
        (cons.PRICE_1500, cons.PRICE_1500)
    ]

    title = models.CharField("Называние скидки", max_length=255)
    price = models.PositiveSmallIntegerField("скидочный цен", choices=PRICE, default=cons.PRICE_1000)
    create_at = models.DateTimeField("Срок начало")
    ending = models.DateField("Срок окончание")
    active = models.BooleanField("Активный", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"
