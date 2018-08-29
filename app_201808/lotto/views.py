#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def name(request):
    return HttpResponse('<h1>나는 자연인이다</h1>')
