from django.contrib import admin

from . models import Post, PostSettings

# Register your models here.
admin.site.register(Post)
admin.site.register(PostSettings)