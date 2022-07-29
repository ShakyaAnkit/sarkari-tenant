from django import forms
from django.contrib.auth.models import Group, User
from .models import *



class RequestedClientForm(forms.ModelForm):
	

	class Meta:
		model = RequestedClient
		fields = ('subdomain', 'name', 'phone_number', 'email', 'organization')

	def clean_phone_number(self):
		phone = self.cleaned_data['phone_number']
		if len(str(phone)) > 10:
			raise forms.ValidationError('Enter a valid mobile number')
		return phone


	def clean_name(self):
		name = self.cleaned_data['name']
		try:
			name = RequestedClient.objects.exclude(pk=self.instance.pk).get(name=name)
		except RequestedClient.DoesNotExist:
			return name.lower()
		raise forms.ValidationError("Name is already taken")


	def clean_subdomain(self):
		subdomain = self.cleaned_data['subdomain']
		try:
			subdomain = RequestedClient.objects.exclude(pk=self.instance.pk).get(subdomain=subdomain)
		except RequestedClient.DoesNotExist:
			return subdomain.lower()
		raise forms.ValidationError("Domain is already taken")


class ClientForm(forms.ModelForm):

	class Meta:
		model = Client
		fields = ('name', 'domain_url', 'schema_name')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

	def clean_domain_url(self):
		data = self.cleaned_data['domain_url']
		# if ".localhost" not in data:
		# 	raise forms.ValidationError("You have forgotten to add .localhost")
		return data

class ClientUserCreateForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
	confirm_password = forms.CharField()

	def clean(self):
		if self.cleaned_data.get('password') != self.cleaned_data.get('confirm_password'):
			raise forms.ValidationError({
				'password': 'Password Confirm Failed',
			})

class LoginForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={'class': 'form-control', 'placeholder':  'Username'}))
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={'class': 'form-control', 'placeholder':  'Password'}))
