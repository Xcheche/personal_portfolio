from django.contrib import admin

# Register your models here.
from .models import Blog
#customize admin
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    search_fields = ('title','description', 'date',)
#register
admin.site.register(Blog, BlogAdmin)
