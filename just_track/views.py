from django.shortcuts import render_to_response, RequestContext
from .models import *

nav = Url.objects.filter(url_type=1)


def home(request):
    points = Location.objects.all()
    return render_to_response(
        'home.html',
        {'nav': nav, 'points': points},
        RequestContext(request)
    )


def api(request):
    return render_to_response(
        'api.html',
        {'nav': nav},
        RequestContext(request)
    )


def help(request):
    return render_to_response(
        'help.html',
        {'nav': nav},
        RequestContext(request)
    )