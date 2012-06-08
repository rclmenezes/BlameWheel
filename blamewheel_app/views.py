# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from blamewheel_app.models import *

def home(request):
    return render_to_response('home.html')