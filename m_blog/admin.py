from django.contrib import admin
from .models import Post
# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    list_display = ("title", "date_create", "text", "files")
    search_fields = ("title", "text")
    date_hierarchy = 'date_create'


admin.site.register(Post, HomeAdmin)


