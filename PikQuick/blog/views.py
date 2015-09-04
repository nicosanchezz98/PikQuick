from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect


from django.conf import settings

# Create your views here.

def home(request):
    context = RequestContext(request)
    #posts = Entrada.objects.all()

    return render_to_response('home.html',
                              context)
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect

# Create your views here.
def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)
