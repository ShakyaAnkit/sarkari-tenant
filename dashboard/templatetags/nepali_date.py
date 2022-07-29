# import os
# import sys
# import datetime
# import pytz

# from django import template
# from django.conf import settings

# from main.DateConverter import DateConverter, NepaliChar

# register = template.Library() 

# def get_request():
# 	import sys
# 	f = sys._getframe()
# 	while f:
# 		request = f.f_locals.get("request")
# 		if request:
# 			return request
# 		f = f.f_back
# 	return None

# def to_local(datetime_obj):
# 	if datetime_obj.tzinfo:
# 		return datetime_obj.astimezone(pytz.timezone(settings.TIME_ZONE))
# 	return datetime_obj.replace(tzinfo=pytz.timezone('UTC')).astimezone(pytz.timezone(settings.TIME_ZONE))

# @register.filter(name='nepali_date') 
# def nepali_date(date):   
# 	request = get_request()
# 	nepali_date_enabled = True if (request.COOKIES.get('nepali_calendar') == 'True' or ( hasattr(request.user, 'personal_profile') and request.user.personal_profile.nep_status == 'True') )  else False
# 	if nepali_date_enabled and (type(date) == datetime.datetime or type(date) == datetime.date):
# 		converter = DateConverter()
# 		converter.setEnglishDate(date.year, date.month, date.day)
# 		if type(date) == datetime.datetime:
# 			date = to_local(date)
# 			return "{} {}, {}, {}".format(NepaliChar.getEnglishMonth(converter.getNepaliMonth()), converter.getNepaliDate(), converter.getNepaliYear(), date.strftime('%I:%M %p'))
# 		elif type(date) == datetime.date:
# 			return "{} {}, {}".format(NepaliChar.getEnglishMonth(converter.getNepaliMonth()), converter.getNepaliDate(), converter.getNepaliYear())
# 	return date