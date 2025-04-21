from django.contrib import admin
from .models import Page

# configuración extra para mi modelo
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Page, PageAdmin)

# Configuracion del Panel
title = "Proyecto con"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle