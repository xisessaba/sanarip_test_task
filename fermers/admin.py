from django.contrib import admin
from .models import Fermer, Culture, Season, Plot


@admin.register(Fermer)
class FermerAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'phone']
    search_fields = ['name', 'description', 'phone']


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = [ 'id','contour','fermer', 'culture', 'season']
    list_filter = ['fermer', 'season']
    search_fields = [ 'fermer', 'culture', 'season']



