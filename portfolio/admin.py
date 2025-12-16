from django.contrib import admin
from .models import Project, Technology, Skill

class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 3

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']
    inlines = [TechnologyInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['category', 'order']
    list_editable = ['order']
