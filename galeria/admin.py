from django.contrib import admin
from galeria.models import Photograph

class ListPhotograph(admin.ModelAdmin):
    list_display = ("id", "name", "legend", "published")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category",)
    list_editable = ("published",)
    list_per_page = 10

admin.site.register(Photograph, ListPhotograph)