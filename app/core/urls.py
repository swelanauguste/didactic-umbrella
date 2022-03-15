from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.TicketListView.as_view(), name="list"),
]
