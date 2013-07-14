from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):

    return render_to_response('althingi/home.html', { 'data': 'Some Data!' }, context_instance = RequestContext(request))
