from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import AdminSite
admin.site.site_header = 'IVAN Schools Administration'
admin.site.site_title = 'IVAN Schools Administration'


class MathAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class EnglishAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class LiteratureAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class BscBtechAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class PHEAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class AgricAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class SocialAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class CivicAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class CRKAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class CreativeArtsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class CreativeWritingAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)


class AbacusAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class SpellingsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class VerbalAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class QuantAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)

class MusicAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    list_per_page = 100
    search_fields = ('title',)


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
