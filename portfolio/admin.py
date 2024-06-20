from django.contrib import admin

# Register your models here.
from .models import Project, Contact


# customize admin
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image", "url")
    search_fields = (
        "title",
        "description",
        "image",
        "url",
    )


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
    search_fields = ("name", "email")


admin.site.register(Contact, ContactAdmin)
# register
admin.site.register(Project, ProjectAdmin)
