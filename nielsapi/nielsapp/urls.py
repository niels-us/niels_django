# from django.urls import path
from . import views

# DOCUMENTACION SWAGGER
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Documentacion de API",
        default_version='v0.1',
        description="Documentacion de ApiRest Equipos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),

    path('', views.index, name='index'),
    path('equipo', views.DetEquipo, name='DetEquipos'),
    path('equipo/<int:pk>', views.Equipos, name='putEquipos'),
    path('usuario', views.DetUsuario, name='DetUsuarios'),
    path('usuario/<int:pk>', views.Usuarios, name='putUsuario'),
    path('integrante', views.DetIntegrante, name='DetIntegrantes'),
    path('integrante/<int:pk>', views.Integrantes, name='putIntegrante'),
    path('descequipo', views.DescEquipo, name='DetEquipos'),
]
