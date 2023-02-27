from django.contrib import admin
from .models import Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "desgination", "created_date")

admin.site.register(Team, TeamAdmin)