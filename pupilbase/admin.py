from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import AdminSite
admin.site.site_header = 'IVAN Schools Administration'
admin.site.site_title = 'IVAN Schools Administration'


class PupilAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'middlename', 'surname')
    list_filter = ('firstname', 'middlename', 'surname')
    list_per_page = 100
    search_fields = ('firstname', 'middlename', 'surname')


admin.site.register(Pupil, PupilAdmin)
