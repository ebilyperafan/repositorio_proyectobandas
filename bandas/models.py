from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nacionalidad(models.Model):
	nombre_nacionalidad= models.CharField(max_length = 200)

	def __str__ (self):
		return self.nombre_nacionalidad
		
class Banda(models.Model):
	nombre_banda = models.CharField(max_length = 100)
	numero_integrantes = models.IntegerField()
	#logo = models.
	nacionalidad =models.ForeignKey(Nacionalidad, on_delete =models.CASCADE)
	photo         = models.ImageField(upload_to='banda', null=True, blank=True)
	
	def __str__ (self):
		return self.nombre_banda


class Rol(models.Model):
	nombre_rol = models.CharField(max_length =100)

	def __str__ (self):
		return self.nombre_rol

class Integrante(models.Model):
	MS ='M'
	FN ='F'
	GENEROS_DE_LAS_PERSONAS_CHOICES=(
		(MS, 'Masculino'),
		(FN, 'Femenino')
		)

	edad = models.IntegerField()
	nombre = models.CharField(max_length = 100)
	genero = models.CharField(max_length=2, choices=GENEROS_DE_LAS_PERSONAS_CHOICES, default=MS)
	roles = models.ManyToManyField(Rol, null = True, blank = True)
	direccion = models.TextField(max_length = 30)
	banda = models.ForeignKey(Banda, on_delete= models.CASCADE)
	foto         = models.ImageField(upload_to='integrante', null=True, blank=True)

	def __str__ (self):
		return self.nombre

'''class Rol_Integrante(models.Model):
	r = models.ForeignKey(Rol)
	i = models.ForeignKey(Integrante)
'''

class Perfil(models.Model):
	user      = models.OneToOneField(User, on_delete=models.CASCADE, null= True, blank=True)
	identificacion = models.CharField(max_length = 100)
	edad        = models.CharField(max_length= 100)
	foto        = models.ImageField(upload_to='perfiles', null=True, blank=True)

	def __str__(self):
		return self.identificacion






