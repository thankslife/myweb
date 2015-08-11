from django.db import models

# Create your models here.
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible

class Column(models.Model):
	name=models.CharField('栏目名称',max_length=256)
	slug=models.CharField('栏目网址',max_length=256,db_index = True)
	intro=models.TextField('栏目简介',default='')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name='栏目'
		verbose_name_plural='栏目'
		ordering = ['name']

class Article(models.Model):
	 column=models.ManyToManyField(Column,verbose_name='归属栏目')
	 title=models.CharField('标题',max_length=256)	
	 slug=models.CharField('网址',max_length=256,db_index=True)	
	 author = models.ForeignKey('auth.User',blank=True,null==True,verbose_name='作者')
	 content = models.TextField('内容',default='',blank=True)
	 published = models.BooleanField('正式发布',default=True)
	 def __str__(self):
	 	return  self.title
	 class Meta:
	 	verbose_name='教程'
	 	verbose_name_plural='教程'
	 	


