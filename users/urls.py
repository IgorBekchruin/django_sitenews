from django.urls import include, path
from django.views.generic import TemplateView

from .views import EmailVerify, Register

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", Register.as_view(), name="register"),
    path('email-confirmed/', TemplateView.as_view(template_name='registration/email_confirmed.html'), name='email_confirmed'),
    path(
        'invalid_verify/',
        TemplateView.as_view(template_name='registration/invalid_verify.html'),
        name='invalid_verify'
    ),
    path(
        'verify_email/<uidb64>/<token>/',
        EmailVerify.as_view(),
        name='verify_email',
    ),
    path(
        'confirm_email/',
        TemplateView.as_view(template_name='registration/confirm_email.html'),
        name='confirm_email'
    ),

]
