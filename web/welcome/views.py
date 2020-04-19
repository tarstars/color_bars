from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    template = loader.get_template('welcome/index.html')
    colors = ['(130, 65, 0)',
              '(200, 200, 0)',
              '(0, 130, 0)',
              '(0, 0, 0)',
              '(130, 0, 70)',
              '(130, 130, 130)',
              '(0, 0, 130)',
              ]
    return HttpResponse(template.render({'colors': colors}, request))


def select_picture(request, user_name):
    template = loader.get_template('welcome/select_picture.html')
    return HttpResponse(template.render({'user_name': user_name}, request))


def guess_picture(request, user_name):
    template = loader.get_template('welcome/guess_picture.html')
    return HttpResponse(template.render({'user_name': user_name}, request))
