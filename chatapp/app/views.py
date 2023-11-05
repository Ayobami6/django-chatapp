from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import SignupForm
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'app/home.html'


class UserCreateView(CreateView):
    form_class = SignupForm
    template_name = "app/signup.html"
    success_url = '/'

    # same as default can comment out

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class LoginInterface(LoginView):
    template_name = 'app/login.html'


class LogoutInterface(LogoutView):
    template_name = 'app/logout.html'
