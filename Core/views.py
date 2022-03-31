from django.shortcuts import render

from .models import Announcements


def test(request):
    context = Announcements.objects.all()
    return render(request, 'Core/index.html', {"obj": context})
