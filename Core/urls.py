from django.urls import path

from .views import AnnouncementsView

urlpatterns = [
    path('', AnnouncementsView.as_view())
]