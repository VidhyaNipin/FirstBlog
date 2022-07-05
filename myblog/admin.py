from django.contrib import admin

# Register your models here.
from myblog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'updated_on', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, BlogPostAdmin)

