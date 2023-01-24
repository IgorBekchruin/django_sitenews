from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'category', 'preview')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width=50>')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
