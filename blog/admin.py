from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):

	fields =  ['title', 'text', 'author']

	search_fields = ['title']


	list_filter = ['title', 'text', 'author']

	list_display = ['title', 'text', 'author']

	list_editable = ['author']





admin.site.register(Post, PostAdmin)
admin.site.register(Comment)