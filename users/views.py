from django.shortcuts import render
from django.views.generic import View
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})