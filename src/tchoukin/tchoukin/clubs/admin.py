from django.contrib import admin
from models import Club


class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']


admin.site.register(Club, ClubAdmin)
