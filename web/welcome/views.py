import glob

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
    context = {'user_name': user_name,
               'pictures': [picture_filename[9:-4] for picture_filename in glob.glob('pictures/*')
                            if 'pictures' in picture_filename]
               }
    return HttpResponse(template.render(context, request))


def guess_picture(request, user_name):
    template = loader.get_template('welcome/guess_picture.html')
    return HttpResponse(template.render({'user_name': user_name}, request))


def return_picture(request, picture_name):
    return HttpResponse(open('pictures/' + picture_name, 'rb').read(), content_type='image/jpeg')


def train_picture(request, user_name, picture_name, color_bars):
    template = loader.get_template('welcome/train_picture.html')
    context = {
        'user_name': user_name,
        'picture_name': picture_name,
        'color_bars': color_bars,
    }
    return HttpResponse(template.render(context, request))
