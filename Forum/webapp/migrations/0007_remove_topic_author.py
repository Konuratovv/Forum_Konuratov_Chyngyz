# Generated by Django 4.2.3 on 2023-07-29 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_comment_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='author',
        ),
    ]
