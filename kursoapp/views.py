from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    d = {'parametro': "Hola mundo!"}
    return render_to_response('home.html', d,context_instance=RequestContext(request))