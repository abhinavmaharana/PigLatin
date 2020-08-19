from django.http import HttpResponse,request
from django.shortcuts import render


def hello (request):
      return HttpResponse("Hello Gunjan!")