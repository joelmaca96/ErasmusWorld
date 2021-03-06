from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin): 
	
	list_display = ('title', 'published_date', 'author')
	list_filter = ['published_date']
	search_fields = ['title']

admin.site.register(Post, PostAdmin)
