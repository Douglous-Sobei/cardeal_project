from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def Thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px; />'.format(object.image.url))
    Thumbnail.short_description = "Image"

    list_display = ("id", "Thumbnail", "first_name", "desgination", "created_date")
    list_display_links = ("id", "Thumbnail", "first_name")
    search_fields = ("first_name", "last_name", "desgination")
    list_filter = ("desgination",)

admin.site.register(Team, TeamAdmin)