from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Equipo, Usuario, Integrante
# import base64

    # readonly_fields=["imagen"]

    # def imagen(self, obj):
        # base64Encoded = base64.b64encode(obj.imagen)
        # return format_html('<img src="data:;base64,{}">', base64Encoded)
        # return "<img src=" + obj.avatar.url + "/>"

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




# class UsuarioAdmin(admin.ModelAdmin):
#     inlines = (IntegranteInline,)
#     list_display = ('pk', 'nombre')
#     list_display_links = ('pk', 'nombre')
#     search_fields = ['nombre']

# formfield_overrides = {
#     BinaryField: {'imagen': BinaryFileInput()},
# }
# readonly_fields = ["imagem_logo", ]

# def imagem_logo(self, obj):
#     base64Encoded = base64.b64encode(obj.logo)
#     return format_html('<img src="data:;base64,{}">', base64Encoded)

# def imagem_logo(self, obj):
#     base64Encoded = base64.b64encode(obj.logo)
#     return mark_safe('<img src="data:;base64,base64Encoded">')


# admin.site.register(Equipo)
# admin.site.register(Usuario)
# admin.site.register(Integrante)
