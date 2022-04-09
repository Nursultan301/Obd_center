from unicodedata import name
from django.urls import path

from .views import TicketDetailView, TicketDetailJsonView

urlpatterns = [
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name="ticket_detail"),
    path('json/ticket/<int:pk>/', TicketDetailJsonView.as_view(), name="ticket_json"),
]