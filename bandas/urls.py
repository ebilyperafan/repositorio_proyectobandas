from django.urls import path
from .views import * 
from django.contrib.auth.models import User


urlpatterns = [
	path('', vista_inicio),
	path('proyecto/',vista_proyecto),
	path('listar_integrante/',vista_listar_integrante, name ='vista_listar_integrante'),
	path('listar_banda/', vista_listar_banda, name =  'vista_listar_banda'),
	path('listar_nacionalidad/', vista_listar_nacionalidad, name = 'vista_listar_nacionalidad'),
	path('listar_rol/', vista_listar_rol, name = 'vista_listar_rol'),
	path('agregar_integrante/',vista_agregar_integrante, name ='vista_agregar_integrante'),
	path('agregar_banda/', vista_agregar_banda, name= 'vista_agregar_banda'),
	path('agregar_nacionalidad/', vista_agregar_nacionalidad, name= 'vista_agregar_nacionalidad'),
	path('agregar_rol/', vista_agregar_rol, name= 'vista_agregar_rol'),
	path('ver_integrante/<int:id_inte>/', vista_ver_integrante, name = 'vista_ver_integrante'),
	path('ver_banda/<int:id_banda>/', vista_ver_banda, name = 'vista_ver_banda'),
	path('ver_naci/<int:id_naci>/', vista_ver_naci, name = 'vista_ver_naci'),
	path('ver_rol/<int:id_rol>/', vista_ver_rol, name = 'vista_ver_rol'),
	path('ver_perfil/',vista_ver_perfil, name= 'vista_ver_perfil'),
	path('editar_integrante/<int:id_inte>/', vista_editar_integrante, name = 'vista_editar_integrante'),
	path('editar_banda/<int:id_banda>/', vista_editar_banda, name = 'vista_editar_banda'),
	path('editar_naci/<int:id_naci>/', vista_editar_nacionalidad, name = 'vista_editar_nacionalidad'),
	path('editar_rol/<int:id_rol>/', vista_editar_rol, name = 'vista_editar_rol'),
	path('eliminar_integrante/<int:id_inte>/', vista_eliminar_integrante, name = 'vista_eliminar_integrante'),
	path('eliminar_banda/<int:id_banda>/', vista_eliminar_banda, name = 'vista_eliminar_banda'),
	path('eliminar_naci/<int:id_naci>/', vista_eliminar_nacionalidad, name = 'vista_eliminar_nacionalidad'),
	path('eliminar_rol/<int:id_rol>/', vista_eliminar_rol, name = 'vista_eliminar_rol'),
	path('login/', vista_login, name = 'vista_login'),
	path('logout/', vista_logout, name = 'vista_logout'),
	path('register/',vista_register, name='vista_register'),
	path('crear_perfil/',vista_crear_perfil, name='vista_crear_perfil'),
	

]