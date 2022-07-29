from django.contrib import admin
from .models import *
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.


for model in apps.get_app_config('dashboard').get_models():
	try:
		admin.site.register(model)
	except AlreadyRegistered:
		pass
