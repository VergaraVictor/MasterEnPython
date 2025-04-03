from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configurar el titulo del panel de admin de django
title= "Master en Python - Victor Vergara 5" 
admin.site.site_header = title
# Configurar subtitulo de admin de django
admin.site.site_title = title
admin.site.index_title = "Panel de Gestión"