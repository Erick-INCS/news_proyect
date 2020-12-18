from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline): #admin.StackedInline
    model = Comment
    extra = 0


class ArtcleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArtcleAdmin)
admin.site.register(Comment)