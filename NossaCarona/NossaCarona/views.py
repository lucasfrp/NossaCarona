from django.http.response import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse(render_to_response('index.html'))