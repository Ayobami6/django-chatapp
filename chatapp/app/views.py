from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import SignupForm
from django.contrib.auth.views import LoginView, LogoutView
import pyrebase


# Create your views here.

firebase_config = {
    "apiKey": "AIzaSyB3eTVLAdHdKtCEFFIrTJXFLTBDD49yu4Q",
    "authDomain": "test-app-4b724.firebaseapp.com",
    "databaseURL": "https://test-app-4b724-default-rtdb.firebaseio.com",
    "projectId": "test-app-4b724",
    "storageBucket": "test-app-4b724.appspot.com",
    "messagingSenderId": "896164659519",
    "appId": "1:896164659519:web:a8f9b0dff23d40a0a6138a",
    "measurementId": "G-X7SH2JF1GK"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()


class HomeView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        name = db.child('data').child('name').get().val()
        gender = db.child('data').child('gender').get().val()
        spec = db.child('data').child('spec').get().val()
        context['name'] = name
        context['gender'] = gender
        context['spec'] = spec
        return context


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
