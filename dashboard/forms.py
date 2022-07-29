from django import forms
from django.http import QueryDict

from .models import *

class LoginForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={'class': 'form-control', 'placeholder':  'Username'}))
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={'class': 'form-control', 'placeholder':  'Password'}))


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields[field].required = True
    
    def clean_email(self):
        email =  self.cleaned_data.get('email')

        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("User with this email address already exists")
        
        return email



# mixins model here
class CategoryForm:
	""" category creation automatically by tags """
	
	def __init__(self, data=None, *args, **kwargs):
		print(data)
		
		if hasattr(self, 'category_model'):
			data = self.check_category(data)
			print(data)
			
		super().__init__(data=data, *args, **kwargs)

	def check_category(self, data):
		if not hasattr(self, 'category_field'):
			self.category_field = 'category'
			
		if data != None:
			data_dict = dict(data)

			data_dict[self.category_field] = list()
			for value in data.getlist(self.category_field):
				try:
					value = int(value)
					data_dict[self.category_field].append(value)
				except:
					if self.category_model.objects.filter(name=value).exists():
						category = self.category_model.objects.filter(name=value).first()
					else:
						category = self.category_model.objects.create(name=value)
					data_dict[self.category_field].append(category.pk)

			data = QueryDict('', mutable=True)
			for key, values in data_dict.items():
				for value in values:
					data.update({ key: value })
		return data


# Models Fields from here

class NoticeForm(forms.ModelForm):
	class Meta:
		model = Notice
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
		
		self.fields['notice_date'].widget.attrs.update({
			'class': 'form-control datepicker'
		})
		self.fields['display_in_marquee'].widget.attrs.update({
			'class': ''
		})


class PressReleaseForm(forms.ModelForm):
	class Meta:
		model = PressRelease
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class BidForm(CategoryForm, forms.ModelForm):
	category_model = BidCategory

	class Meta:
		model = Bid
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class PublicationForm(CategoryForm, forms.ModelForm):
	category_model = PublicationCategory
	category_field = 'category'
	
	class Meta:
		model = Publication
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})


class PolicyForm(CategoryForm, forms.ModelForm):
	category_model = PolicyCategory

	class Meta:
		model = Policy
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})


class DownloadForm(CategoryForm, forms.ModelForm):
	category_model = DownloadCategory

	class Meta:
		model = Download
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

		self.fields['start_date'].widget.attrs.update({
			'class': 'form-control datepicker'
		})

		self.fields['end_date'].widget.attrs.update({
			'class': 'form-control datepicker'
		})

	def clean(self):
		start_date = self.cleaned_data.get('start_date')
		end_date = self.cleaned_data.get('end_date')
		if end_date != None and end_date < start_date:
			raise forms.ValidationError({
				'end_date': 'End date must be greater than start date',
			})

class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class HRForm(forms.ModelForm):
	class Meta:
		model = HR
		exclude = ('priority', 'created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

		self.fields['date_of_birth'].widget.attrs.update({
			'class': 'form-control datepicker'
		})

		self.fields['show_in_slider'].widget.attrs.update({
			'class': ''
		})

		self.fields['show_in_homepage'].widget.attrs.update({
			'class': ''
		})

		self.fields['suchana_adhikari'].widget.attrs.update({
			'class': ''
		})

class SliderForm(forms.ModelForm):
	class Meta:
		model = Slider
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})


class AlbumForm(forms.ModelForm):
	photos = forms.ImageField(required=False)

	class Meta:
		model = Album
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

		self.fields['photos'].widget.attrs.update({
			'multiple': True
		})

class AlbumPhotosForm(forms.ModelForm):
	photos = forms.ImageField(required=False)
	
	class Meta:
		model = AlbumPhoto
		fields = []

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['photos'].widget.attrs.update({
			'multiple': True,
			'class': 'form-control',
		})

class AlbumPhotoForm(forms.ModelForm):

	class Meta:
		model = AlbumPhoto
		exclude = ('album', 'created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class UsefulLinkForm(forms.ModelForm):
	class Meta:
		model = UsefulLink
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class PageForm(forms.ModelForm):
	class Meta:
		model = Page
		exclude = ('add_to_navbar', 'created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
		
		self.fields['page_margin'].widget.attrs.update({
			'class': ''
		})
		

class NavbarForm(forms.ModelForm):
	class Meta:
		model = Navbar
		exclude = ('priority', 'created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

class HomePagePopupForm(forms.ModelForm):
	class Meta:
		model = HomePagePopup
		exclude = ('is_active', 'created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})


class SiteConfigForm(forms.ModelForm):
	class Meta:
		model = SiteConfig
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			if('full_nav' in field):
				continue
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
		self.fields['latitude'].widget.attrs.update({
			'class': 'form-control',
			'readonly': True,
		})
		self.fields['longitude'].widget.attrs.update({
			'class': 'form-control',
			'readonly': True,
		})


class ListForm(CategoryForm, forms.ModelForm):
	category_model = ListCategory

	class Meta:
		model = List
		exclude = ('created_by', 'deleted_at')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})