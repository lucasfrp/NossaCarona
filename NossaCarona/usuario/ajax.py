from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from models import Usuario
from django.contrib.auth.models import User as DjangoUser
from datetime import datetime

@dajaxice_register
def login_with_fb(request, response):
    dajax = Dajax()
    '''
    try:
        usuario = Usuario.objects.get(fb_id=response['id'])
    except Usuario.DoesNotExist:
        userdjango = DjangoUser.objects.create_user(response['email'], response['email'], response['id'])
        userdjango.first_name = response['first_name']
        userdjango.last_name = response['last_name']
        userdjango.save()
        usuario = Usuario(user=userdjango, sexo=response['gender'][0], fb_id=response['id'], dt_nascimento=datetime.strptime(response['birthday'],'%m/%d/%Y'))
        usuario.save()
    request.session['user_id'] = usuario.pk
    dajax.redirect('/')
    '''
    print response
    return dajax.json()
    