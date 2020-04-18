from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    result = '<h1>Welcome to our color bars project</h1>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(130, 65, 0);stroke-width:0;stroke:rgb(0,0,0)" />' \
             '</svg>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(200, 200, 0);stroke-width:0;stroke:rgb(0,0,0)" />' \
             '</svg>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(200, 0, 0);stroke-width:0;stroke:rgb(0,0,0)" />' \
             '</svg>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(0, 130, 0);stroke-width:0;stroke:rgb(0,0,0)" />' \
             '</svg>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(0, 0, 0);stroke-width:0;stroke:rgb(0,0,0)" />' \
             '</svg>'             \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(130, 0, 70);stroke-width:0;stroke:rgb(0,0,0)" />' \
             '</svg>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(130, 130, 130);stroke-width:0;stroke:rgb(0,0,0)" />' \
             '</svg>' \
             '<svg width="400" height="110">' \
             '<rect width="300" height="100" style="fill:rgb(0, 0, 130);stroke-width:0;stroke:rgb(0,0,0)" />' \
             '</svg>'

    return HttpResponse(result)
