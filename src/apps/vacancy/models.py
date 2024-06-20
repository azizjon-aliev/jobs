import uuid

from django.db import models


class Vacancy(models.Model):
	id = models.UUIDField(
		default=uuid.uuid4,
		unique=True,
		primary_key=True,
		editable=False
	)
	title = models.CharField(max_length=255)
	description = models.TextField()
	salary = models.FloatField()
	company = models.ForeignKey('Company', on_delete=models.CASCADE)
	skills = models.ManyToManyField('Skill', related_name='vacancies')

	def __str__(self):
		return self.title


class Company(models.Model):
	id = models.UUIDField(
		default=uuid.uuid4,
		unique=True,
		primary_key=True,
		editable=False
	)
	name = models.CharField(max_length=255)
	description = models.TextField()
	city = models.CharField(max_length=255)
	address = models.TextField()

	def __str__(self):
		return self.name


class Skill(models.Model):
	id = models.UUIDField(
		default=uuid.uuid4,
		unique=True,
		primary_key=True,
		editable=False
	)
	name = models.CharField(max_length=255)
	description = models.TextField()

	def __str__(self):
		return self.name
