from django.db import models

CHOICES = (
	('Video', 'Видео'),
	('Image', 'Изображение'),
) 

CHOICES_TRACK = (
	('0', 'Разрешено'),
	('2', 'Запрешено'),
	('1', 'Опасно'),
) 

## Create your models here.
class News(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField(default=' ')
	content  = models.TextField(default=' ')
	date = models.DateField(auto_now=False,auto_now_add=False)
	image = models.ImageField(upload_to="media/uploads",max_length=100,default='')

class Track(models.Model):
	name = models.CharField(max_length=300)
	status = models.CharField(max_length=30,choices=CHOICES_TRACK)


class Event(models.Model):
	name = models.CharField(max_length=30)
	date = models.DateField(auto_now=False, auto_now_add=False)
	description = models.TextField(default=' ' )
	image = models.ImageField(upload_to="media/uploads",max_length=100,default='')

class PlayListAdvertising(models.Model):
	name = models.CharField(max_length=300)
	advertisings = models.ManyToManyField('Advertising')

class Advertising(models.Model):
	name = models.CharField(max_length=300)
	count = models.IntegerField(default=0)
	file = models.FileField()
	active = models.BooleanField(default=False)
	type = models.CharField(max_length=30,choices=CHOICES)
	time= models.IntegerField(default=0)
	def __str__(self):
		return self.name		

class Category (models.Model):
	name = models.CharField(max_length=30,default='')
	def __str__(self):
		return self.name
class Shop(models.Model):
	name = models.CharField(max_length=250,default='')
	category = models.ForeignKey('Category',default='')
	description = models.TextField(default='')
	location = models.CharField(max_length=100,default='')
	image = models.ImageField(upload_to="media/uploads",max_length=100,default='')
	def __str__(self):
		return self.name