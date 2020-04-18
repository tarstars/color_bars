from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    result = '<h1>Welcome to our color bars project</h1>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(0, 0, 255);stroke-width:3;stroke:rgb(0,0,0)" />' \
             '</svg>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(0, 255, 0);stroke-width:3;stroke:rgb(0,0,0)" />' \
             '</svg>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(255, 0, 0);stroke-width:3;stroke:rgb(0,0,0)" />' \
             '</svg>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(255, 255, 0);stroke-width:3;stroke:rgb(0,0,0)" />' \
             '</svg>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(255, 0, 255);stroke-width:3;stroke:rgb(0,0,0)" />' \
             '</svg>'             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(0,255,255);stroke-width:3;stroke:rgb(0,0,0)" />' \
             '</svg>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(127, 127, 127);stroke-width:3;stroke:rgb(0,0,0)" />' \
             '</svg>'

    return HttpResponse(result)
