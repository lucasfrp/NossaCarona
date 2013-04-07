from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response


def login(request):
    if request.session.get('user_id'):
        return HttpResponseRedirect('/')
    return HttpResponse(render_to_response('login.html'))