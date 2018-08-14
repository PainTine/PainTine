# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Tableau.models import *
# Register your models here.
class TableauModelAdmin(admin.ModelAdmin):
    
    list_display = ["Nom", "Longueur", "Largueur", "Nature", "Realisateur"]
    list_display_links = ["Nom", "Longueur", "Largueur", "Nature", "Realisateur"]
    list_filter = ["Nom", "Longueur", "Largueur", "Nature", "Realisateur"]
    search_fields = ["Nom", "Longueur", "Largueur", "Nature", "Realisateur"]

    class Meta:
    	model = Tableau

class TechniqueModelAdmin(admin.ModelAdmin):
    
    list_display = ["Nature", "Description"]
    list_display_links = ["Nature"]
    list_filter = ["Nature"]
    search_fields = ["Nature", "Description"]

    class Meta:
    	model = Technique

admin.site.register(Tableau, TableauModelAdmin)
admin.site.register(Technique, TechniqueModelAdmin)
