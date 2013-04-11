from models import Usuario
from django.contrib.auth.backends import ModelBackend

class FbBackend(ModelBackend):
    
    def authenticate(self, fb_id):
        try:
            usuario = Usuario.objects.get(fb_id = fb_id)
            return usuario.user
        except Usuario.DoesNotExist:
            return None