import glob
import random

from django.http import HttpResponse

# Create your views here.
from django.template import loader
from django.utils import timezone

from utility.color_bars import parse_set_string, exclude_from, Palette
from welcome.models import TrainRecord


def index(request):
    template = loader.get_template('welcome/index.html')
    colors = map(str, map(Palette.get_color_by_index, Palette.get_indices()))
    return HttpResponse(template.render({'colors': colors}, request))


def select_picture(request, user_name):
    template = loader.get_template('welcome/select_picture.html')

    random_permutation = Palette.get_indices()
    random.shuffle(random_permutation)

    context = {'user_name': user_name,
               'random_permutation': '_'.join(map(str, random_permutation)),
               'pictures': [picture_filename[9:-4] for picture_filename in glob.glob('pictures/*')
                            if 'pictures' in picture_filename]
               }
    return HttpResponse(template.render(context, request))


def guess_picture(request, user_name):
    template = loader.get_template('welcome/guess_picture.html')
    return HttpResponse(template.render({'user_name': user_name}, request))


def return_picture(request, picture_name):
    return HttpResponse(open('pictures/' + picture_name, 'rb').read(), content_type='image/jpeg')


def train_picture(request, user_name, picture_name, color_bars, initial_permutation):
    template = loader.get_template('welcome/train_picture.html')
    demonstrate, memorize = parse_set_string(color_bars)

    if demonstrate:
        list_of_choices = [(exclude_from(demonstrate, bar), memorize + [bar], bar) for bar in demonstrate]
        list_of_choices = [{'demonstrate': '_'.join(map(str, demonstrate)),
                            'permutation': '_'.join(map(str, permutation)),
                            'link': '__'.join('_'.join(map(str, part)) for part in (demonstrate, permutation)),
                            'color': Palette.get_color_by_index(color_index),
                            } for demonstrate, permutation, color_index in list_of_choices]

        context = {
            'user_name': user_name,
            'picture_name': picture_name,
            'color_bars': color_bars,
            'list_of_choices': list_of_choices
        }
        return HttpResponse(template.render(context, request))

    tr = TrainRecord(dt=timezone.now(),
                     user_name=user_name,
                     picture_name=picture_name,
                     permutation='_'.join(map(str, memorize)),
                     initial_permutation=initial_permutation,
                     )
    tr.save()

    template = loader.get_template('welcome/after_submit.html')
    return HttpResponse(template.render({}, request))


def show_database(request):
    template = loader.get_template('welcome/display_database.html')
    return HttpResponse(template.render({'train_records': TrainRecord.objects.all()}, request))
