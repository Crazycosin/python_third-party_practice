# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from forms import AddForm
# Create your views here.

def index(request):
    return HttpResponse("HELLO DJANGO!")


def add_calc(request):
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponse(sum([int(a), int(b)]))


def add_calc2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def home(request):
    return render(request, 'home.html')


def add_form(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(a+b))
        else:
            form = AddForm()
        return render(request, 'add_form.html', {'form': form})

