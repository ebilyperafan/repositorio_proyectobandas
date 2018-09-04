from django import forms
from .models import *
from django.contrib.auth.models import User

class proyecto_form(forms.Form):
	categoria =(
		("pop","k-pop"),
		("bacha","Bachata"),
		("regue","Regueton")
		)
	edad = (
		 ("niños","10-15"),
		 ("adole","16-21"),
		 ("adul","22-30")
		 )
	check =(
		("1"," Mujeres"),
		("2","Hombres"),
		("3","Mixto")
		)
	nombre 		=forms.CharField(widget= forms.TextInput())
	descripcion =forms.CharField(widget= forms.Textarea())
	categoria 	=forms.MultipleChoiceField(widget=forms.Select,choices=categoria)
	edad 		=forms.MultipleChoiceField(widget=forms.Select,choices=edad)
	genero		=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=check)
	fecha 		=forms.DateTimeField(widget= forms.TimeInput())

class agregar_integrante_form(forms.ModelForm):
	class Meta:
		model = Integrante
		fields = ['nombre','edad','genero','roles','direccion','banda','foto']
		widgets={
		'nombre'       : forms.TextInput(attrs={"class":"form-control"}),
		'edad' 			: forms.TextInput(attrs={"class":"form-control"}),
		'genero'       : forms.SelectMultiple(attrs={"class":"form-control"}),
		'roles'        : forms.SelectMultiple(attrs={"class":"form-control"}),
		'direccion'        : forms.TextInput(attrs={"class":"form-control"}),
		'banda'        : forms.SelectMultiple(attrs={"class":"form-control"}),
		'foto'        : forms.FileInput(),

		
		}


class agregar_banda_form(forms.ModelForm):
	class Meta:
		model = Banda
		fields = ['nombre_banda', 'numero_integrantes','nacionalidad','photo']
		widgets={
		'nombre_banda': forms.TextInput(attrs={"class":"form-control"}),
		'numero_integrantes': forms.TextInput(attrs={"class":"form-control"}),
		'nacionalidad': forms.SelectMultiple(attrs={"class":"form-control"}),
		'photo': forms.FileInput(),
		
		
		}


class agregar_nacionalidad_form(forms.ModelForm):
	class Meta:
		model = Nacionalidad
		fields = ['nombre_nacionalidad']
		widgets={
		'nombre_nacionalidad': forms.TextInput(attrs={"class":"form-control"}),
		
		}


class agregar_rol_form(forms.ModelForm):
	class Meta:
		model = Rol 
		fields =['nombre_rol']
		widgets={
		'nombre_rol'       : forms.TextInput(attrs={"class":"form-control"}),
		
		}


class login_form(forms.Form):
	usuario = forms.CharField(widget= forms.TextInput(attrs={"class":"form-control"}))
	contraseña = forms.CharField(widget= forms.PasswordInput(render_value = False, attrs={"class":"form-control"}))

class register_form(forms.Form):
	username    = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	email       = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
	password_1  = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False, attrs={"class":"form-control"}))
	password_2  = forms.CharField(label='Confirmar Password',widget=forms.PasswordInput(render_value=False, attrs={"class":"form-control"}))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			us = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya Registrado')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			email = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Correo Electronico ya Existe')

	def clean_password_2(self):
		password_1 = self.cleaned_data['password_1']
		password_2 = self.cleaned_data['password_2']

		if password_1 == password_2:
			pass
		else:
			raise forms.ValidationError('Passwords no coinciden')

class perfil_form(forms.ModelForm):
	class Meta:
		model = Perfil
		fields =['identificacion','edad','foto']
		widgets={
		'identificacion' : forms.TextInput(attrs={"class":"form-control"}),
		'edad'        : forms.TextInput(attrs={"class":"form-control"}),
		'foto'        : forms.FileInput(),
		
		}





