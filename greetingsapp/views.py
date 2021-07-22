from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def welcomePage(request):
    return HttpResponse("<strong>welcome in django</strong>")


def nameStudent(request):
    return HttpResponse("<h1>My name is akash yadav</h1>")


def friendsList(request):
    f_list = "<ol><li>Avind</li>,<li>kailesh</li>,<li>Himashu</li></ol>"
    obj = HttpResponse(f_list)
    return obj
