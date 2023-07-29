from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from webapp.forms import TopicForm
from webapp.models import Topic


class TopicView(ListView):
    model = Topic
    template_name = "topics/index.html"
    context_object_name = 'topics'
    paginate_by = 10


class CreateTopic(CreateView):
    model = Topic
    form_class = TopicForm
    template_name = 'topics/create_topic.html'

    def get_success_url(self):
        return reverse('webapp:topics')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailedTopic(DetailView):
    model = Topic
    template_name = 'topics/detailed_topic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self.get_object()
        comments = topic.comments.all()
        context['comments'] = comments
        return context
