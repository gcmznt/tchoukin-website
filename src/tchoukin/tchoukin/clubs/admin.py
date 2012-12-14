from django.contrib import admin
from models import Club


class ClubAdmin(admin.ModelAdmin):
	pass


admin.site.register(Club, ClubAdmin)
