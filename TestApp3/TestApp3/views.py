from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import employee
from django.http import HttpResponse

@login_required
def test(request):
    e=employee()
    e.name="Ahmed2"
    e.address="Giza"
    e.age=29
    e.save()
    return HttpResponse("Shall be saved by " + request.user.username)
