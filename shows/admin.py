from django.contrib import admin

# Register your models here.
from .models import Column,Article
class ColumnAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display=('name','slug','intro',)
class ArticleAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display=('title','slug','author','pub_date','update_time')
admin.site.register(Column,ColumnAdmin)
admin.site.register(Article,ArticleAdmin)

