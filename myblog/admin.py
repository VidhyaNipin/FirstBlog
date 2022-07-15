from django.contrib import admin

# Register your models here.
from myblog.models import BlogPost, Comment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'updated_on', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, BlogPostAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blogpost', 'created_on', 'email', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments', 'reject_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

    def reject_comments(self, request, queryset):
        queryset.update(active=False)


admin.site.register(Comment, CommentsAdmin)


