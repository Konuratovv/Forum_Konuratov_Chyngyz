from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import login_view, logout_view, RegisterView, ProfileView

app_name = "accounts"

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('<int:pk>/profile/', ProfileView.as_view(), name="profile"),
]