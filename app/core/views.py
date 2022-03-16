from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Ticket


class TicketListView(ListView):
    model = Ticket


class TicketCreateView(CreateView):
    model = Ticket
    fields = "__all__"


class TicketDetailView(DetailView):
    model = Ticket
