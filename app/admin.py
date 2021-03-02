from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "fish")
    list_display_links = ("id", "fish")


admin.site.register(Post, PostAdmin)
