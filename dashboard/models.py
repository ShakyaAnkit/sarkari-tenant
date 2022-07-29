from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db import connection

from jsonfield import JSONField
from ckeditor.fields import RichTextField
from easy_thumbnails.files import get_thumbnailer

from home.lang.utils import get_locale
from home.templatetags.nepaliDate import dateInToNepali

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
		return self.has_extension('.pdf') or self.has_extension('.docX')

	@property
	def file_image(self):
		if self.is_image:
			return settings.STATIC_URL + 'home/assets/images/jpg.svg'
		elif self.is_pdf:
			return settings.STATIC_URL + 'home/assets/images/pdf.svg'
		else:
			return settings.STATIC_URL + 'home/assets/images/others.svg'


class ModelTranslationMixin:
	@property
	def name__localized(self):
		if get_locale() == 'ne' or self.name_en == None:
			return self.name
		return self.name_en
	
	@property
	def title__localized(self):
		if get_locale() == 'ne' or self.title_en == None:
			return self.title
		return self.title_en

	@property
	def created_at__localized(self):
		if get_locale() == 'en':
			return self.created_at.date()
		return dateInToNepali(self.created_at)

	@property
	def updated_at__localized(self):
		if get_locale() == 'en':
			return self.updated_at.date()
		return dateInToNepali(self.updated_at)


def get_tenant_upload_folder(instance, filename):
	"""
	creates custom folders for tenant
	"""
	upload_folder = '{}/{}/{}'.format(
		connection.tenant.schema_name,
		instance._meta.verbose_name_plural.title().lower().replace(' ', '-'),
		filename,
	)
	return upload_folder


class Notice(ModelTranslationMixin, FileTypeMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	description = RichTextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='notices', null=True, blank=True)
	notice_date = models.DateField(null=True, blank=True)
	display_in_marquee = models.BooleanField('Display in Marquee', default=False)


	class Meta:
		ordering = ('-notice_date', '-id')

	def save(self, *args, **kwargs):
		if self.notice_date == None:
			if self.created_at != None:
				self.notice_date = self.created_at.date()
			else:
				self.notice_date = timezone.now().date()
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.title

	@property
	def notice_date__localized(self):
		if get_locale() == 'en':
			return self.notice_date
		return dateInToNepali(self.notice_date)



class PressRelease(ModelTranslationMixin, FileTypeMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	description = RichTextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='press-releases', null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title


class BidCategory(ModelTranslationMixin, DateTimeModel):
	name = models.CharField(max_length=255)
	name_en = models.CharField('Name (English)', max_length=255, null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.name

class Bid(ModelTranslationMixin, FileTypeMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	category = models.ForeignKey(BidCategory, null=True, blank=True, related_name='bids', on_delete=models.CASCADE)
	description = RichTextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='bids', null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title

		
class PublicationCategory(ModelTranslationMixin, DateTimeModel):
	name = models.CharField(max_length=255)
	name_en = models.CharField('Name (English)', max_length=255, null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.name


class Publication(ModelTranslationMixin, FileTypeMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	category = models.ForeignKey(PublicationCategory, null=True, blank=True, related_name='publications', on_delete=models.CASCADE)
	description = RichTextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='publications', null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title



class PolicyCategory(ModelTranslationMixin, DateTimeModel):
	name = models.CharField(max_length=255)
	name_en = models.CharField('Name (English)', max_length=255, null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.name

class Policy(ModelTranslationMixin, FileTypeMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	category = models.ForeignKey(PolicyCategory, null=True, blank=True, related_name='policies', on_delete=models.CASCADE)
	description = RichTextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='policies', null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title


class DownloadCategory(ModelTranslationMixin, DateTimeModel):
	name = models.CharField(max_length=255)
	name_en = models.CharField('Name (English)', max_length=255, null=True, blank=True)

	class Meta:
		ordering = ('-id',)
    
	def get_downloads(self):
		return self.downloads.filter(deleted_at=None)
    
	def __str__(self):
		return self.name
		
class Download(ModelTranslationMixin, FileTypeMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	category = models.ForeignKey(DownloadCategory, null=True, blank=True, related_name='downloads', on_delete=models.CASCADE)
	description = RichTextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='downloads', null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title


class Project(ModelTranslationMixin, FileTypeMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	description = RichTextField(null=True, blank=True)
	budget_amout = models.CharField(max_length=255, null=True, blank=True)
	document_file = models.FileField('File', upload_to='project-and-budgets', null=True, blank=True)
	# preview if PDF/Image else download

	class Meta:
		ordering = ('-id',)
	
	def __str__(self):
		return self.title


class Event(ModelTranslationMixin, FileTypeMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	description = RichTextField(null=True, blank=True)
	start_date = models.DateField()
	end_date = models.DateField(null=True, blank=True)
	location = models.CharField(max_length=255)
	location_en = models.CharField('Location (English)', max_length=1024, null=True, blank=True)
	document_file = models.FileField('File', upload_to='events', null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title

	@property
	def location__localized(self):
		if get_locale() == 'ne' or self.location_en == None:
			return self.location
		return self.location_en

	@property
	def start_date__localized(self):
		if get_locale() == 'en':
			return self.start_date
		return dateInToNepali(self.start_date)

	@property
	def end_date__localized(self):
		if get_locale() == 'en':
			return self.end_date
		return dateInToNepali(self.end_date)


class News(ModelTranslationMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	sub_title = models.CharField(max_length=1024, null=True, blank=True)
	description = RichTextField(null=True, blank=True)
	photo = models.ImageField('Photo', upload_to='news', null=True, blank=True)
	author = models.CharField(max_length=512, null=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title

	def get_photo(self):
		return get_thumbnailer(self.photo)['small_landscape'].url if self.photo else settings.STATIC_URL+'home/assets/images/govern-logo.png'

	def get_original_photo(self):
		return self.photo.url if self.photo else settings.STATIC_URL+'home/assets/images/govern-logo.png'


class HR(ModelTranslationMixin, DateTimeModel):
	name = models.CharField(max_length=255)
	name_en = models.CharField('Name (English)', max_length=1024, null=True, blank=True)
	photo = models.ImageField('Photo', upload_to='hr', null=True, blank=True)
	position = models.CharField(max_length=255)
	position_en = models.CharField('Position (English)', max_length=255, null=True, blank=True)
	level = models.CharField(max_length=255, null=True, blank=True)
	date_of_birth = models.DateField(null=True, blank=True)
	phone_no = models.CharField('Telephone no.', max_length=255, null=True, blank=True)
	email = models.CharField(max_length=255, null=True, blank=True)
	contact_address = models.TextField(null=True, blank=True)
	permanent_address = models.TextField(null=True, blank=True)
	description = RichTextField(null=True, blank=True)
	show_in_slider = models.BooleanField(default=False)
	show_in_homepage = models.BooleanField(default=True)
	suchana_adhikari = models.BooleanField(default=False)
	priority = models.PositiveIntegerField(default=0)

	class Meta:
		ordering=['priority', '-id']

	def __str__(self):
		return self.name

	def get_photo(self):
		return get_thumbnailer(self.photo)['hr_thumbnail'].url if self.photo else 'http://nepal.gov.np/splash/nepal-govt.png'

	def get_original_photo(self):
		return self.photo.url if self.photo else ''

	@property
	def position__localized(self):
		if get_locale() == 'ne' or self.position_en == None:
			return self.position
		return self.position_en

	@property
	def date_of_birth__localized(self):
		if get_locale() == 'en':
			return self.date_of_birth
		return dateInToNepali(self.date_of_birth)


class Slider(ModelTranslationMixin, DateTimeModel):
	title = models.CharField(max_length=1024, null=True, blank=True)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	photo = models.ImageField('Photo', upload_to='sliders')

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title

	def get_photo(self):
		return get_thumbnailer(self.photo)['slider_thumbnail'].url if self.photo else settings.STATIC_URL+'home/assets/images/govern-logo.png'

class Album(ModelTranslationMixin, DateTimeModel):
	name = models.CharField(max_length=255)
	name_en = models.CharField('Name (English)', max_length=255, null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.name
	
	def get_title_image(self):
		album = self.albums.filter(deleted_at__isnull=True).first()
		if album:
			return get_thumbnailer(album.photo)['small_landscape'].url if album.photo else ''
		else:
			return ''
		
class AlbumPhoto(DateTimeModel):
	album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='albums')
	photo = models.ImageField('Photo', upload_to='photos')

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		if self.photo:
			return self.photo.name
		return 'No photo'

	def get_photo(self):
		return get_thumbnailer(self.photo)['small_landscape'].url if self.photo else ''

	def get_original_photo(self):
		return self.photo.url if self.photo else ''

class Department(ModelTranslationMixin, DateTimeModel):
	""" SubsidiaryDepartment """
	name = models.CharField(max_length=255)
	name_en = models.CharField('Name (English)', max_length=255, null=True, blank=True)
	website = models.CharField(max_length=255, null=True, blank=True)
	description = RichTextField(null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.name


class UsefulLink(ModelTranslationMixin, DateTimeModel):
	name = models.CharField(max_length=255)
	name_en = models.CharField('Name (English)', max_length=255, null=True, blank=True)
	link = models.CharField(max_length=255)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.name


class Message(DateTimeModel):
	name = models.CharField(max_length=255)
	phone_no = models.CharField(max_length=255)
	email = models.EmailField(null=True, blank=True)
	message = models.TextField()
	# captcha = models.CharField(max_length=255)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.name


class Page(ModelTranslationMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	slug = models.CharField(max_length=255)
	photo = models.ImageField('Photo', upload_to='pages', null=True, blank=True)
	description = RichTextField()
	add_to_navbar = models.BooleanField(default=False)
	page_margin = models.BooleanField(default=True)
	
	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title

	def get_photo(self):
		return self.photo.url if self.photo else ''

class Navbar(ModelTranslationMixin, DateTimeModel):
	title = models.CharField(max_length=50)
	title_en = models.CharField('Title (English)', max_length=50, null=True, blank=True)
	url = models.CharField(max_length=50, help_text='/pages/1/')
	parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)
	priority = models.PositiveIntegerField(default=0)

	class Meta:
		ordering=['priority', 'id']

	def __str__(self):
		return self.title

	def get_children(self):
		return self.children.filter(deleted_at__isnull=True)

	@property
	def url__localized(self):
		if get_locale() == 'ne' or not self.url.startswith('/'):
			return self.url
		return '/en'+self.url


class HomePagePopup(ModelTranslationMixin, DateTimeModel):
	title = models.CharField(max_length=255)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	photo = models.ImageField('Photo', upload_to='popups')
	is_active = models.BooleanField(default=True)
	
	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title

	def get_photo(self):
		return self.photo.url if self.photo else ''



class SiteConfig(DateTimeModel):
	header = models.CharField(max_length=1024)
	header_en = models.CharField('Header (English)', max_length=1024, null=True, blank=True)
	main_title = models.CharField(max_length=1024)
	main_title_en = models.CharField('Mail title (English)', max_length=1024, null=True, blank=True)
	sub_title = models.CharField(max_length=1024)
	sub_title_en = models.CharField('Sub title (English)', max_length=1024, null=True, blank=True)
	title_address = models.CharField(max_length=1024)
	title_address_en = models.CharField('Title address (English)', max_length=1024, null=True, blank=True)
	website_title = models.CharField(max_length=1024)
	website_title_en = models.CharField('Website title (English)', max_length=1024, null=True, blank=True)
	logo = models.ImageField(upload_to='logos')
	about_us = RichTextField()
	about_us_en = RichTextField('About us (English)', null=True, blank=True)
	address = models.TextField()
	email = models.EmailField()
	phone_no = models.CharField(max_length=255)
	fax = models.CharField(max_length=255, null=True, blank=True)
	audio_notice_board = models.CharField(max_length=255, null=True, blank=True)
	pobox = models.CharField('P.O. Box no.', max_length=255, null=True, blank=True)
	full_nav = models.BooleanField('Navbar Full Width', default=False)
	facebook = models.CharField(max_length=255, null=True, blank=True)
	twitter = models.CharField(max_length=255, null=True, blank=True)
	hr_string = models.CharField('HR String', max_length=255, null=True, blank=True)
	hr_string_en = models.CharField('HR String (English)', max_length=255, null=True, blank=True)
	header_iframe = models.TextField(null=True, blank=True)
	latitude = models.CharField(max_length=255, null=True, blank=True)
	longitude = models.CharField(max_length=255, null=True, blank=True)
	# add other extra fields here

	def __str__(self):
		return self.header

	def save(self, *args, **kwargs):
		if self.pk == None and SiteConfig.objects.all().count() > 0:
			return None
		return super().save(*args, **kwargs)

	def get_logo(self):
		return self.logo.url if self.logo else 'http://nepal.gov.np/splash/nepal-govt.png'


	@staticmethod
	def get_instance():
		if SiteConfig.has_object():
			return SiteConfig.objects.first()
		return SiteConfig()

	@staticmethod
	def has_object():
		return SiteConfig.objects.all().count() > 0
	
	# localization

	@property
	def header__localized(self):
		if get_locale() == 'ne' or self.header_en == None:
			return self.header
		return self.header_en

	@property
	def main_title__localized(self):
		if get_locale() == 'ne' or self.main_title_en == None:
			return self.main_title
		return self.main_title_en

	@property
	def sub_title__localized(self):
		if get_locale() == 'ne' or self.sub_title_en == None:
			return self.sub_title
		return self.sub_title_en

	@property
	def title_address__localized(self):
		if get_locale() == 'ne' or self.title_address_en == None:
			return self.title_address
		return self.title_address_en

	@property
	def website_title__localized(self):
		if get_locale() == 'ne' or self.website_title_en == None:
			return self.website_title
		return self.website_title_en

	@property
	def about_us__localized(self):
		if get_locale() == 'ne' or self.about_us_en == None:
			return self.about_us
		return self.about_us_en

	@property
	def hr_string__localized(self):
		if get_locale() == 'ne' or self.hr_string_en == None:
			return self.hr_string
		return self.hr_string_en



class ListCategory(ModelTranslationMixin, DateTimeModel):
	name = models.CharField(max_length=255)
	name_en = models.CharField('Name (English)', max_length=255, null=True, blank=True)
	show_in_suchana = models.BooleanField(default=False)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.name

class List(ModelTranslationMixin, FileTypeMixin, DateTimeModel):
	title = models.CharField(max_length=1024)
	title_en = models.CharField('Title (English)', max_length=1024, null=True, blank=True)
	category = models.ForeignKey(ListCategory, null=True, blank=True, related_name='list', on_delete=models.CASCADE)
	description = RichTextField(null=True, blank=True)
	document_file = models.FileField('File', upload_to='list', null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.title

		