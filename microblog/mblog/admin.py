from django.contrib import admin

from .models import MBlog
class MBlogAdmin(admin.ModelAdmin) : 
    list_display = ('__unicode__', 'content', 'time')

admin.site.register(MBlog, MBlogAdmin)