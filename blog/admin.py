from django.contrib import admin
from blog.models import Post, ZipCode
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']

admin.site.register(Post, PostAdmin)

class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'city', 'gu', 'dong', 'road']

admin.site.register(ZipCode, ZipCodeAdmin)