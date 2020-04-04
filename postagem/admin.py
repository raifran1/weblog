from django.contrib import admin
from .models import Postagem

# Register your models here.

@admin.register(Postagem)
class PostAdmin(admin.ModelAdmin):
   list_display = ('titulo', 'dt_publicacao', 'status')
   search_fields = ('titulo', 'conteudo')
   list_filter = ('titulo','dt_criacao', 'dt_publicacao', 'autor')
   raw_id_fields = ('autor',)
