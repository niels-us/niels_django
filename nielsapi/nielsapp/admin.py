from django.contrib import admin
# Register your models here.
from .models import Equipo,Usuario,Integrante
admin.site.register(Equipo)
admin.site.register(Usuario)
admin.site.register(Integrante)
