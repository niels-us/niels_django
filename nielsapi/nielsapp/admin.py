from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Equipo, Usuario, Integrante


@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'equipo', 'usuario', 'UsuarioEquipo', 'fecha')
    list_display_links = ('pk', 'equipo')
    search_fields = ['equipo']


class IntegranteInline(admin.TabularInline):
    model = Integrante


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    inlines = (IntegranteInline,)
    list_display = ('pk', 'nombre')
    list_display_links = ('pk', 'nombre')
    search_fields = ['nombre']


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    inlines = (IntegranteInline,)
    list_display = ('pk', 'nombre', 'imagen')
    list_display_links = ('pk', 'nombre')
    search_fields = ['nombre']


# admin.site.register(Equipo)
# admin.site.register(Usuario)
# admin.site.register(Integrante)
