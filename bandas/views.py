from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
def vista_proyecto(request):
	info_enviado=False
	name = ""
	descripcion= ""
	catego =""
	age =""
	sex =""
	date =""
	
	if request.method == "POST":
		formulario = proyecto_form(request.POST)
		if formulario.is_valid():
			info_enviado =True
			name = formulario.cleaned_data['nombre']
			descripcion = formulario.cleaned_data['integrantes']
			catego = formulario.cleaned_data['categoria']
			age = formulario.cleaned_data['edad']
			sex = formulario.cleaned_data['sexo']
			date = formulario.cleaned_data['fecha']
	else:	
		formulario= proyecto_form()
	return render(request,'proyecto.html',locals())

def vista_listar_integrante(request):
	listar_integrante = Integrante.objects.all()
	return render(request, 'listar_integrante.html', locals())

def vista_listar_banda(request):
	listar_banda = Banda.objects.all()
	return render(request, 'listar_banda.html',locals())

def vista_listar_nacionalidad(request):
	listar_nacionalidad = Nacionalidad.objects.all()
	return render(request, 'listar_nacionalidad.html',locals())

def vista_listar_rol(request):
	listar_rol = Rol.objects.all()
	return render(request, 'listar_rol.html', locals())

def vista_ver_perfil(request):
	ver_perfil = Perfil.objects.get(user = request.user)
	#ver_perfil = Perfil.objects.all()
	return render(request, 'ver_perfil.html', locals())


def vista_agregar_integrante(request):
	if request.method =='POST':
		formulario= agregar_integrante_form(request.POST, request.FILES)
		if formulario.is_valid():
			integrante = formulario.save(commit = False)
			integrante.status = True
			integrante.save()
			formulario.save_m2m()
			return redirect ('/listar_integrante/')
	else:
		formulario = agregar_integrante_form()
	return render(request,'agregar_integrante.html',locals())

def vista_agregar_banda(request):
	if request.method =="POST":
		formulario = agregar_banda_form(request.POST, request.FILES)
		if formulario.is_valid():
			banda = formulario.save(commit = False)
			banda.status = True
			banda.save()
			formulario.save_m2m()
			return redirect ('/listar_banda/')
	else: 
		formulario = agregar_banda_form()
	return render(request, 'agregar_banda.html', locals())
	
def vista_agregar_nacionalidad(request):
	if request.method =="POST":
		formulario = agregar_nacionalidad_form(request.POST, request.FILES)
		if formulario.is_valid():
			naci = formulario.save(commit = False)
			naci.status = True
			naci.save()
			formulario.save_m2m()
			return redirect ('/listar_nacionalidad/')
	else: 
		formulario = agregar_nacionalidad_form()
	return render(request, 'agregar_naci.html', locals())
	
def vista_agregar_rol(request):
	if request.method == "POST":
		formulario = agregar_rol_form(request.POST, request.FILES)
		if formulario.is_valid():
			rol1 = formulario.save(commit = False)
			rol1.status = True 
			rol1.save()
			formulario.save_m2m()
			return redirect('/listar_rol/')
	else: 
		formulario = agregar_rol_form()
	return render(request, 'agregar_rol.html', locals())	
	

def vista_ver_integrante(request, id_inte):
	p = Integrante.objects.get(id = id_inte)
	print(p)
	return render(request,'ver_integrante.html', locals())

def vista_ver_banda(request, id_banda):
	p = Banda.objects.get(id = id_banda)
	integrantes=Integrante.objects.filter(banda=p)
	print(p)
	return render(request, 'ver_banda.html', locals())

def vista_ver_naci(request, id_naci):
	p = Nacionalidad.objects.get(id = id_naci)
	print(p)
	return render(request, 'ver_naci.html', locals())

def vista_ver_rol(request, id_rol):
	p = Rol.objects.get(id = id_rol)
	print(p)
	return render(request, 'ver_rol.html', locals())

def vista_editar_integrante(request, id_inte):
	inte = Integrante.objects.get(id=id_inte)
	if request.method =="POST":
		formulario = agregar_integrante_form(request.POST, request.FILES, instance=inte)
		if formulario.is_valid():
			inte = formulario.save()
			return redirect('/listar_integrante/')

	else:
		formulario = agregar_integrante_form(instance = inte)
	return render(request, 'agregar_integrante.html', locals())
	
def vista_editar_banda(request, id_banda):
	banda= Banda.objects.get(id=id_banda)
	if request.method =="POST":
		formulario = agregar_banda_form(request.POST, request.FILES, instance=banda)
		if formulario.is_valid():
			banda = formulario.save()
			return redirect('/listar_banda/')

	else:
		formulario = agregar_banda_form(instance = banda)
	return render(request, 'agregar_banda.html', locals())

def vista_editar_nacionalidad(request, id_naci):
	naci = Nacionalidad.objects.get(id=id_naci)
	if request.method =="POST":
		formulario = agregar_nacionalidad_form(request.POST, request.FILES, instance=naci)
		if formulario.is_valid():
			naci = formulario.save()
			return redirect('/listar_nacionalidad/')

	else:
		formulario = agregar_nacionalidad_form(instance = naci)
	return render(request, 'agregar_naci.html', locals())

def vista_editar_rol(request, id_rol):
	rol1 = Rol.objects.get(id=id_rol)
	if request.method =="POST":
		formulario = agregar_rol_form(request.POST, request.FILES, instance=rol1)
		if formulario.is_valid():
			rol1 = formulario.save()
			return redirect('/listar_rol/')

	else:
		formulario = agregar_rol_form(instance = rol1)
	return render(request, 'agregar_rol.html', locals())

def vista_eliminar_integrante(request, id_inte):
	inte = Integrante.objects.get(id = id_inte)
	inte.delete()
	return redirect('/listar_integrante/')

def vista_eliminar_banda(request, id_banda):
	banda = Banda.objects.get(id= id_banda)
	banda.delete()
	return redirect('/listar_banda/')

def vista_eliminar_nacionalidad(request, id_naci):
	naci = Nacionalidad.objects.get(id =id_naci)
	naci.delete()
	return redirect('/listar_nacionalidad/')

def vista_eliminar_rol(request, id_rol):
	rol1 = Rol.objects.get(id= id_rol)
	rol1.delete()
	return redirect('/listar_rol/')


def vista_login(request):
	usu =""
	cla =""
	if request.method == "POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['contraseña']
			usuario = authenticate(username =usu, password=cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj = "usuario o contraseña incorrectas"
	formulario = login_form()
	return render(request, 'login.html', locals())
	

def vista_logout(request):
	logout(request)
	return redirect('/login/')

def vista_inicio(request):
	return render(request,'inicio.html', locals())


def vista_register(request):
	formulario = register_form()
	if request.method == 'POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['username']
			correo  = formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			us = User.objects.create_user(username = usuario, email= correo, password = password_1)
			us.save()
			return render(request, 'tanks_for_register.html', locals())
		else:
			return render(request, 'register.html', locals())
	return render(request, 'register.html', locals())

def vista_crear_perfil(request):
	form_1 = register_form()
	form_2 = perfil_form()
	if request.method=='POST':
		form_1 = register_form(request.POST)
		form_2 = perfil_form(request.POST, request.FILES)
		if form_1.is_valid() and form_2.is_valid():
			usuario = form_1.cleaned_data['username']
			correo  = form_1.cleaned_data['email']
			password_1 = form_1.cleaned_data['password_1']
			password_2 = form_1.cleaned_data['password_2']
			us = User.objects.create_user(username = usuario, email= correo, password = password_1)
			us.save()
			
			y = form_2.save(commit=False)
			y.user = us
			y.save()
			msg ="Gracias por registrarse"
			return redirect('/login/')

	return render(request, 'crear_perfil.html', locals())




