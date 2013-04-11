from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import get_user

def index(request):
    from usuario.models import Usuario
    #user = Usuario.objects.get(pk=request.session['user_id']) if request.session.get('user_id') else None    
    return HttpResponse(render_to_response('index.html',{'user':get_user(request)}))

def channel(request):
    return HttpResponse(render_to_response('facebook/channel.html'))