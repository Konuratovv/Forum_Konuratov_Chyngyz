from django.urls import path

from webapp.views.comment_views import CommentCreateView, CommentUpdateView, CommentDeleteView
from webapp.views.topic_views import TopicView, CreateTopic, DetailedTopic

app_name = "webapp"

urlpatterns = [
    path('', TopicView.as_view(), name='topics'),
    path('create/', CreateTopic.as_view(), name='topic_create'),
    path('topic/<int:pk>/details/', DetailedTopic.as_view(), name='topic_detail'),

    path('topic/<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment')
]