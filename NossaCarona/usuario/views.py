from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Usuario
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import authenticate, login as userlogin, logout as userlogout

def login(request):
    from datetime import datetime 
    from pyfb import Pyfb
    from NossaCarona.settings import FACEBOOK_APP_ID, FACEBOOK_SECRET_KEY, FACEBOOK_REDIRECT_URL_LOGIN
    if request.GET.get('code'): #Login WITH facebook
        code =  request.GET['code']
        facebook = Pyfb(FACEBOOK_APP_ID)
        facebook.get_access_token(FACEBOOK_SECRET_KEY, code, redirect_uri=FACEBOOK_REDIRECT_URL_LOGIN)
        me = facebook.get_myself()
        userdjango = authenticate(fb_id=me.id)
        if not userdjango:
            userdjango = DjangoUser.objects.create_user(me.email, me.email, None)
            userdjango.first_name = me.first_name
            userdjango.last_name = me.last_name
            userdjango.save()
            usuario = Usuario(user=userdjango, sexo=me.gender[0], fb_id=me.id, dt_nascimento=datetime.strptime(me.birthday,'%m/%d/%Y'))
            usuario.save()
        userlogin(request,userdjango)
    else: #login WITHOUT facebook
        pass
    return HttpResponseRedirect('/')

def logout(request):
    userlogout(request)
    return HttpResponseRedirect('/')

def novousuario(request):
    return HttpResponse(render_to_response('novousuario.html'))