from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars', verbose_name='Аватар')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
