from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Topic, Comment


class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = "comments/comment_create.html"

    def form_valid(self, form):
        topic = get_object_or_404(Topic, pk=self.kwargs.get("pk"))
        comment = form.save(commit=False)
        comment.topic = topic
        comment.author = self.request.user
        comment.save()
        topic_comment, is_created = topic.objects.get_or_create(comment=comment)
        if is_created:
            topic_comment.qty += 1
        topic_comment.save()
        return redirect("webapp:topic_detail", pk=topic.pk)


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/update_comment.html"

    def get_success_url(self):
        return reverse("webapp:topic_detail", kwargs={"pk": self.object.topic.pk})


class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse("webapp:topic_detail", kwargs={"pk": self.object.topic.pk})

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
