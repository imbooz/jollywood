from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.utils import timezone

class UserProfile(User):
	levels = [
		('Beginner', 'Beginner'),
		('Elementary', 'Elementary'),
		('Pre-Intermediate', 'Pre-Intermediate'),
		('Intermediate', 'Intermediate'),
		('Upper-Intermediate', 'Upper-Intermediate'),
		('Advanced', 'Advanced'),
	]

	courses = [
		('English', 'English'),
		('Russian', 'Russian'),
		('Mathematics', 'Mathematics'),

	]

	titles = [
		('Teacher', 'Teacher'),
		('Student', 'Student'),
	]

	icons = [
		('fa-user', 'User'),
		('fa-user-graduate', 'Student'),
		('fa-user-ninja', 'Ninja'),
		('fa-user-tie', 'Tie'),
		('fa-user-md', 'Doctor'),
		('fa-user-astronaut', 'Astronaut'),
		('fa-user-secret', 'Spy'),
		('fa-user-injured', 'Injured'),
	]

	bio = models.TextField(blank=True, null=True)
	country = models.CharField(max_length = 100, blank=True, null=True)
	course = models.CharField(
		max_length = 20,
		choices=courses,
		default='English',
	)
	level = models.CharField(
		max_length = 20,
		choices=levels,
		default='Beginner',
	)
	title = models.CharField(
		max_length = 20,
		choices=titles,
		default='Student',
	)
	avatar = models.ImageField(default='avatars/default_avatar.jpg', upload_to='avatars')
	icon = models.CharField(
		max_length = 150,
		choices = icons,
		default = 'fa-user'
	)
	instagram = models.CharField(max_length = 100, blank=True, null=True)
	facebook = models.CharField(max_length = 100, blank=True, null=True)
	twitter = models.CharField(max_length = 100, blank=True, null=True)
	telegram = models.CharField(max_length = 100, blank=True, null=True)

	def is_student(self):
		return self.title == 'Student'


	def is_teacher(self):
		return self.title == 'Teacher'

	def get_absolute_url(self):
		return reverse('user-profile', kwargs={'slug': self.username})

	def __str__(self):
		return f'{self.username} Profile'

	def save(self, **kwargs):
		super().save()

		img = Image.open(self.avatar.path)

		if img.height != img.width:
			w = img.width
			h = img.height

			if h > w:
				a = h - w
				box = (a/2, a/2, w, w)
			else:
				a = w - h
				box = (a/2, a/2, h, h)

			img = img.crop(box)

			if img.height > 500 or img.width > 500:
				output_size = (500, 500)
				img.thumbnail(output_size)
				img.save(self.avatar.path)
			else:
				img.save(self.avatar.path)


class Status(models.Model):
	text = models.TextField(blank=True)
	img = models.ImageField(blank=True, null=True, upload_to='userstatuses')
	likes = models.PositiveIntegerField(default=0)
	time = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Status'
		verbose_name_plural = 'Statuses'
		ordering = ['-id']



	def __str__(self):
		return f'No {self.id} Status by {self.owner.username}'


	def save(self, **kwargs):
		super().save()

		img = Image.open(self.img.path)

		if img.height > 500 or img.width > 500:
			output_size = (500, 500)
			img.thumbnail(output_size)
			img.save(self.img.path)
		else:
			img.save(self.img.path)
