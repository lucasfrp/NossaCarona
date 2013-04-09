from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response


def login(request):
    if request.session.get('user_id'):
        return HttpResponseRedirect('/')
    return HttpResponse(render_to_response('login.html'))

def logout(request):
    del request.session['user_id']
    return HttpResponseRedirect('/')

def novousuario(request):
    return HttpResponse(render_to_response('novousuario.html'))