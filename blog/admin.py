from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'published_date')

# Register your models here.

admin.site.register(Post, PostAdmin)