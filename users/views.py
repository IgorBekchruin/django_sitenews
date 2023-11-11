import json
from django.contrib.auth import authenticate, login
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator as \
    token_generator
from django.utils.http import urlsafe_base64_decode

from .models import User

from .tasks import send_activate_email_message_task

from .forms import UserCreationForm


class Register(View):
    template_name = "registration/register.html"

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            current_site = get_current_site(request)
            domain = current_site.domain
            post_dict = {}
            post_dict['domain'] = domain
            post_dict['user_id'] = user.id
            json_data = json.dumps(post_dict)
            send_activate_email_message_task.delay(json_data)
            return redirect('confirm_email')

        context = {'form': form}

        return render(request, self.template_name, context)


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('email_confirmed')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user

