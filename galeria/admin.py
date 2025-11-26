from django.contrib import admin
from galeria.models import Fotografia

class ListarObjetos(admin.ModelAdmin):
    list_display = ('id','nome','legenda','publicado')
    list_display_links = ('nome','id')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_per_page = 10
    list_editable = ('publicado',)
    

admin.site.register(Fotografia, ListarObjetos)