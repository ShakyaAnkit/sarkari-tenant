from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from jsonfield import JSONField

AUDIT_TYPE_CHOICES = (
	(1, 'LOGIN'),
	(2, 'LOGOUT'),
	(3, 'CREATE'),
	(4, 'UPDATE'),
	(5, 'DELETE'),
)
AUDIT_CHOICES = dict(AUDIT_TYPE_CHOICES)

# Create your models here.
class AuditTrial(models.Model):
	modelType = models.CharField('Model Type', max_length=255)
	objectId = models.IntegerField('Model Obj Id')
	action = models.IntegerField(choices=AUDIT_TYPE_CHOICES, default=0, null=False)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	ip = models.GenericIPAddressField(null=True)
	fromObj = JSONField(null=True)
	toObj = JSONField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.modelType) +' '+ str(dict(AUDIT_TYPE_CHOICES)[self.action]) + ' by : ' + str(self.user.username)


class DateTimeModel(models.Model):
	created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False,)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True,)
	deleted_at = models.DateTimeField(null=True, blank=True)

	class Meta:
		abstract = True

	def delete(self, hard=False, *args, **kwargs):
		if hard:
			return super().delete(*args, **kwargs)
		self.deleted_at = timezone.now()
		self.save(update_fields=['deleted_at'])


#
# Dashboard Models here
#

class FileTypeMixin:
	def has_extension(self, extension):
		if self.document_file:
			return self.document_file.name.lower().endswith(extension)
		return False

	@property
	def is_image(self):
		return self.has_extension('.jpg') or self.has_extension('.jpeg') or self.has_extension('.png') or self.has_extension('.gif')

	@property
	def is_pdf(self):
		return self.has_extension('.pdf')


class Notice(FileTypeMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	description = models.TextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='notices', null=True, blank=True)

	def __str__(self):
		return self.title


class PressRelease(FileTypeMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	description = models.TextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='press-releases', null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title


class BidCategory(DateTimeModel):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Bid(DateTimeModel):
	title = models.CharField(max_length=1024)
	category = models.ForeignKey(BidCategory, null=True, blank=True, related_name='bids', on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='bids', null=True, blank=True)

	def __str__(self):
		return self.title

		
class PublicationCategory(DateTimeModel):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Publication(DateTimeModel):
	title = models.CharField(max_length=1024)
	category = models.ForeignKey(PublicationCategory, null=True, blank=True, related_name='publications', on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='publications', null=True, blank=True)

	def __str__(self):
		return self.title



class PolicyCategory(DateTimeModel):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Policy(DateTimeModel):
	title = models.CharField(max_length=1024)
	category = models.ForeignKey(PolicyCategory, null=True, blank=True, related_name='policies', on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='policies', null=True, blank=True)

	def __str__(self):
		return self.title


class DownloadCategory(DateTimeModel):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Download(DateTimeModel):
	title = models.CharField(max_length=1024)
	category = models.ForeignKey(DownloadCategory, null=True, blank=True, related_name='downloads', on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='downloads', null=True, blank=True)

	def __str__(self):
		return self.title


class Project(DateTimeModel):
	title = models.CharField(max_length=1024)
	description = models.TextField(null=True, blank=True)
	budget_amout = models.CharField(max_length=255, null=True, blank=True)
	document_file = models.FileField('File', upload_to='project-and-budgets', null=True, blank=True)
	# preview if PDF/Image else download

	def __str__(self):
		return self.title


class Event(DateTimeModel):
	title = models.CharField(max_length=1024)
	description = models.TextField(null=True, blank=True)
	start_date = models.DateField()
	end_date = models.DateField(null=True, blank=True)
	location = models.CharField(max_length=255)
	document_file = models.FileField('File', upload_to='events', null=True, blank=True)

	def __str__(self):
		return self.title


class News(DateTimeModel):
	title = models.CharField(max_length=1024)
	sub_title = models.CharField(max_length=1024, null=True, blank=True)
	description = RichTextField(null=True, blank=True)
	photo = models.ImageField('Photo', upload_to='news', null=True, blank=True)
	author = models.CharField(max_length=512, null=True)

	def __str__(self):
		return self.title

	def get_photo(self):
		return self.photo.url if self.photo else settings.STATIC_URL+'home/assets/images/govern-logo.png'


class HR(DateTimeModel):
	name = models.CharField(max_length=255)
	photo = models.ImageField('Photo', upload_to='hr', null=True, blank=True)
	position = models.CharField(max_length=255)
	level = models.CharField(max_length=255)
	phone_no = models.CharField(max_length=255, null=True, blank=True)
	email = models.CharField(max_length=255, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	show_in_slider = models.BooleanField(default=False)
	priority = models.PositiveIntegerField(default=0)

	class Meta:
		ordering=['priority', 'id']

	def __str__(self):
		return self.name

	def get_photo(self):
		return self.photo.url if self.photo else ''

class Slider(DateTimeModel):
	title = models.CharField(max_length=1024, null=True, blank=True)
	photo = models.ImageField('Photo', upload_to='sliders')

	def __str__(self):
		return self.title

	def get_photo(self):
		return self.photo.url if self.photo else ''

class Album(DateTimeModel):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name
	
	def get_title_image(self):
		album = self.albums.filter(deleted_at__isnull=True).first()
		if album:
			return album.photo.url if album.photo else ''
		else:
			return ''
		
class AlbumPhoto(DateTimeModel):
	album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='albums')
	photo = models.ImageField('Photo', upload_to='photos')

	def __str__(self):
		if self.photo:
			return self.photo.name
		return 'No photo'

	def get_photo(self):
		return self.photo.url if self.photo else ''

class Department(DateTimeModel):
	""" SubsidiaryDepartment """
	name = models.CharField(max_length=255)
	website = models.CharField(max_length=255, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name


class UsefulLink(DateTimeModel):
	name = models.CharField(max_length=255)
	link = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Message(DateTimeModel):
	name = models.CharField(max_length=255)
	phone_no = models.CharField(max_length=255)
	email = models.EmailField(null=True, blank=True)
	message = models.TextField()
	captcha = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Page(DateTimeModel):
	title = models.CharField(max_length=1024)
	slug = models.CharField(max_length=255)
	photo = models.ImageField('Photo', upload_to='pages', null=True, blank=True)
	description = models.TextField()
	add_to_navbar = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_photo(self):
		return self.photo.url if self.photo else ''

class Navbar(DateTimeModel):
	title = models.CharField(max_length=50)
	url = models.CharField(max_length=50, help_text='/pages/1/')
	parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)
	priority = models.PositiveIntegerField(default=0)

	class Meta:
		ordering=['priority', 'id']

	def __str__(self):
		return self.title


class HomePagePopup(DateTimeModel):
	title = models.CharField(max_length=255)
	photo = models.ImageField('Photo', upload_to='popups')
	
	def __str__(self):
		return self.title

	def get_photo(self):
		return self.photo.url if self.photo else ''

class SiteConfig(DateTimeModel):
	header = models.CharField(max_length=1024)
	main_title = models.CharField(max_length=1024)
	sub_title = models.CharField(max_length=1024)
	website_title = models.CharField(max_length=1024)
	logo = models.ImageField(upload_to='logos')
	about_us = RichTextField()
	address = models.TextField()
	email = models.EmailField()
	phone_no = models.CharField(max_length=255)
	fax = models.CharField(max_length=255, null=True, blank=True)
	audio_notice_board = models.CharField(max_length=255, null=True, blank=True)
	pobox = models.CharField('P.O. Box no.', max_length=255, null=True, blank=True)
	# add other extra fields here

	def __str__(self):
		return self.header

	def save(self, *args, **kwargs):
		if self.pk == None and SiteConfig.objects.all().count() > 0:
			return None
		return super().save(*args, **kwargs)

	@staticmethod
	def get_instance():
		if SiteConfig.has_object():
			return SiteConfig.objects.first()
		return SiteConfig()

	@staticmethod
	def has_object():
		return SiteConfig.objects.all().count() > 0