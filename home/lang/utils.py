import os
import json

LANG_DICT = {}

def get_request():
	import sys
	f = sys._getframe()
	while f:
		request = f.f_locals.get("request")
		if request:
			return request
		f = f.f_back
	return None

def get_locale():
	request = get_request()
	return 'en' if request.path.startswith('/en/') else 'ne'

def load_locale_dict(locale):
	if locale in LANG_DICT:
		return 

	json_path = 'home/lang/{}.json'.format(locale)
	if os.path.exists(json_path):
		print('LOADING JSON PATH', json_path)
		try:
			with open(json_path) as json_file:
				lang_dict = json.load(json_file)
				LANG_DICT[locale] = lang_dict
				return
		except:
			pass
	
	# creating empty dict
	LANG_DICT[locale] = {}


def translate(text):
	locale = get_locale()
	load_locale_dict(locale)
	return LANG_DICT[locale].get(text.lower().strip(), text)

