from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.TicketListView.as_view(), name="list"),
    path("add/", views.TicketCreateView.as_view(), name="create"),
    path("ticket/<slug:slug>/", views.TicketDetailView.as_view(), name="detail"),
]
