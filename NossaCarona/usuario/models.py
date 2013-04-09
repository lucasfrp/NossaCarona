from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	user = models.OneToOneField(User)
	sexo = models.CharField(max_length=1)
	fb_id = models.IntegerField(null=True, blank=True)
	dt_nascimento = models.DateField()
	
	def __unicode__(self):
		return self.user.first_name