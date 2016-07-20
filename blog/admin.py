from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
admin.site.register(Post, PostAdmin)