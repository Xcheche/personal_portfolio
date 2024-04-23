from django.contrib import admin

# Register your models here.
from .models import Project
#customize admin
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'url')
    search_fields = ('title','description', 'image', 'url',)
#register
admin.site.register(Project, ProjectAdmin)
