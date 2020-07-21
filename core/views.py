from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    context = {"home": "active"}
    return render(request, 'core/home.html', context)


def jan_mohr(request):
    context = {"jan_mohr": "active"}
    return render(request, 'core/jan_mohr.html', context)


def error(request):
    context = {"error": "active"}
    return render(request, 'core/error.html', context)
