from django.urls import path

from .views import UserListView, RegisterView

urlpatterns = [
    path("users/", UserListView.as_view(), name="users"),
    path("register/", RegisterView.as_view(), name="register"),
]