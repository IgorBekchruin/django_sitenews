from django.contrib.auth import views
from django.urls import include, path

from .views import Register

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", Register.as_view(), name="register"),
]
