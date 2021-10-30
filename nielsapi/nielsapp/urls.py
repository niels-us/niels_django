from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),   
    path('equipo',views.DetEquipo,name='DetEquipos'),
    path('equipo/<int:pk>',views.Equipos,name='putEquipos'),
    path('usuario',views.DetUsuario,name='DetUsuarios'),
    path('usuario/<int:pk>',views.Usuarios,name='putUsuario'),
    path('integrante',views.DetIntegrante,name='DetIntegrantes'),
    path('integrante/<int:pk>',views.Integrantes,name='putIntegrante'),
]
