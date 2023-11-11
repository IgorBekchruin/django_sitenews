import json
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.shortcuts import get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as \
    token_generator

from .models import User


def send_email_for_verify(data):
    normal_data = json.loads(data)
    user_id = normal_data['user_id']
    user = get_object_or_404(User, id=user_id)
    context = {
        'user': user,
        'domain': normal_data['domain'],
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
    }
    message = render_to_string(
        'registration/verify_email.html',
        context=context,
    )
    email = EmailMessage(
        'Veryfi email',
        message,
        to=[user.email],
    )
    email.send()