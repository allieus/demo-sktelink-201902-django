from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'short_content', 'is_publish', 'tags', 'created_at']
    list_display_links = ['title']
    list_filter = ['is_publish']
    search_fields = ['title']

    def short_content(self, post):
        return post.content[:20] + ' ...'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
