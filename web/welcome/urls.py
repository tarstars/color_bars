from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/select_picture/<str:user_name>', views.select_picture, name='select_picture'),
    path('welcome/guess_picture/<str:user_name>', views.guess_picture, name='guess_picture'),
]
