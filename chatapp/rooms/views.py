from django.shortcuts import render
from .models import Room
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here


class RoomListView(ListView, LoginRequiredMixin):
    model = Room
    context_object_name = 'rooms'
    template_name = "room/rooms.html"


class RoomDetailView(DetailView):
    model = Room
    context_object_name = 'room'
    template_name = "room/room_detail.html"
