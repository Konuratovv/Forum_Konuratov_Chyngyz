# Generated by Django 4.2.3 on 2023-07-29 11:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_topic_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='qty',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Количество'),
        ),
    ]
