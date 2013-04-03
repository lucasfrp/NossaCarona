from django.db import models

class Usuario(models.Model):
	nome = models.CharField(max_length=50)
	sobrenome = models.CharField(max_length=50)
	email = models.EmailField()
	sexo = models.CharField(max_length=1)
