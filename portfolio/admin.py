from django.contrib import admin
from .models import Project, Technology, Skill, BlogPost, BlogCategory

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

class BlogCategoryInline(admin.TabularInline):
    model = BlogCategory
    extra = 2

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'created_date', 'updated_date']
    list_filter = ['published', 'created_date', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['published']
    inlines = [BlogCategoryInline]
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)