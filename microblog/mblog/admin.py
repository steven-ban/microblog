from django.contrib import admin

from .models import MBlog
class MBlogAdmin(admin.ModelAdmin) : 
    list_display = ('content', )

admin.site.register(MBlog, MBlogAdmin)