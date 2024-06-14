from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import AdminSite
admin.site.site_header = 'IVAN Schools Administration'
admin.site.site_title = 'IVAN Schools Administration'


class MathAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class EnglishAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class LiteratureAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class BscBtechAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class PHEAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class AgricAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class SocialAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class CivicAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class CRKAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class CreativeArtsAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class CreativeWritingAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)


class AbacusAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class SpellingsAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class VerbalAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class QuantAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)

class MusicAdmin(admin.ModelAdmin):
    list_display = ('pupil',)
    list_filter = ('pupil',)
    list_per_page = 100
    search_fields = ('pupil',)


admin.site.register(MusicScores, MusicAdmin)
admin.site.register(HistoryScores, HistoryAdmin)
admin.site.register(QuantitativeReasoningScores, QuantAdmin)
admin.site.register(VerbalReasoningScores, VerbalAdmin)
admin.site.register(SpellingsScores, SpellingsAdmin)
admin.site.register(AbacusScores, AbacusAdmin)
admin.site.register(CreativeWritingScores, CreativeWritingAdmin)
admin.site.register(CreativeArtsScores, CreativeArtsAdmin)
admin.site.register(CRKScores, CRKAdmin)
admin.site.register(CivicEducationScores, CivicAdmin)
admin.site.register(SocialStudiesScores, SocialAdmin)
admin.site.register(AgriculturalScienceScores, AgricAdmin)
admin.site.register(PHEScores, PHEAdmin)
admin.site.register(ComputerStudiesScores, ComputerAdmin)
admin.site.register(BasicSciTechScores, BscBtechAdmin)
admin.site.register(EnglishLiteratureScores, LiteratureAdmin)
admin.site.register(EnglishScores, EnglishAdmin)
admin.site.register(MathematicsScores, MathAdmin)
