from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('titulo', 'slug', 'status', 'creado_el')
    list_filter=("status",)
    search_fields=['title', 'content']
    prepopulated_fields={'slug': ('titulo',)    }
admin.site.register(Post, PostAdmin)