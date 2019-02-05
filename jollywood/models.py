from django.db import models
from django.utils import timezone
from user.models import UserProfile
from PIL import Image


class Post(models.Model):
	title = models.CharField(max_length = 150)
	auth = models.ForeignKey('user.UserProfile', on_delete=models.CASCADE)
	content_shown = models.TextField()
	content_hidden = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	read = models.PositiveIntegerField()
	liked = models.PositiveIntegerField()
	thumbnail = models.ImageField(default='post_thumbs/default_thumb.jpg', upload_to='post_thumbs')
		
	def save(self, **kwargs):
		super().save()

		img = Image.open(self.thumbnail.path)

		if img.height > 500 or img.width > 500:
			output_size = (500, 500)
			img.thumbnail(output_size)
			img.save(self.thumbnail.path)
		else:
			img.save(self.thumbnail.path)

	def __str__(self):
		return self.title


def file_upload_path(instance, filename):
	return 'books/{0}/{1}'.format(instance.level, filename)


class Books(models.Model):
	levels = [
		('Beginner', 'Beginner'),
		('Elementary', 'Elementary'),
		('Pre', 'Pre-Intermediate'),
		('Intermediate', 'Intermediate'),
		('Upper', 'Upper-Intermediate'),
		('Advanced', 'Advanced'),
	]

	categories = [
		('Grammar', 'Grammar'),
		('Vocabulary', 'Vocabulary'),
		('Story', 'Story'),
	]

	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200, blank=True, null=True)
	description = models.TextField()
	level = models.CharField(
		max_length = 20,
		choices=levels,
		default='Beginner',
	)
	category = models.CharField(
		max_length = 20,
		choices=categories,
		default='Grammar'
	) 
	cover = models.ImageField(default='book_thumbs/default_cover.jpg', upload_to='book_thumbs')
	book = models.FileField(upload_to=file_upload_path)


	def save(self, **kwargs):
		super().save()

		img = Image.open(self.cover.path)

		if img.height > 500 or img.width > 500:
			output_size = (500, 500)
			img.thumbnail(output_size)
			img.save(self.cover.path)
		else:
			img.save(self.cover.path)


	def __str__(self):
		return f'{self.title} in {self.category}; Level: {self.level}'