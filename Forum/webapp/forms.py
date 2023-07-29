from django import forms
from django.forms import widgets

from webapp.models import Topic, Comment


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
