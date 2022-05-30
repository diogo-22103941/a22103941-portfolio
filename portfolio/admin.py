from django.contrib import admin
from .models import *

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','data')

class PontosAdmin(admin.ModelAdmin):
    list_display = ('nome','pontos')

admin.site.register(Post,PostsAdmin)
admin.site.register(PontuacaoQuizz,PontosAdmin)
admin.site.register(Cadeira)
admin.site.register(Projeto)