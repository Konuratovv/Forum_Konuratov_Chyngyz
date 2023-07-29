from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название", unique=True, null=False, blank=False)
    description = models.TextField(max_length=2000, verbose_name="Описание", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT,
                               default=1, related_name="topics", verbose_name="Автор")
    qty = models.PositiveIntegerField(verbose_name="Количество", default=0, validators=(MinValueValidator(0),))

    def str(self):
        return f"{self.id} {self.title}"

    class Meta:
        db_table = "topics"
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class Comment(models.Model):
    topic = models.ForeignKey("webapp.Topic", related_name="comments", on_delete=models.CASCADE, verbose_name='Тема')
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.ForeignKey('auth.User', on_delete=models.SET_DEFAULT,
                               default=1, related_name="comments", verbose_name="Автор")

    def __str__(self):
        return self.text[:20]
