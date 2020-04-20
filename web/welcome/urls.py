from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/select_picture/pictures/<str:picture_name>', views.return_picture, name='return_picture'),
    path('welcome/select_picture/welcome/train_picture/<str:user_name>/<str:bare_picture_name>/pictures/<str:picture_name>', views.return_picture, name='return_picture'),
    path('welcome/select_picture/<str:user_name>', views.select_picture, name='select_picture'),
    path('welcome/guess_picture/<str:user_name>', views.guess_picture, name='guess_picture'),
    path('welcome/select_picture/welcome/train_picture/<str:user_name>/<str:picture_name>/<str:color_bars>',
         views.train_picture, name='train_picture'),
    path('welcome/show_database', views.show_database, name='show_database')
]
