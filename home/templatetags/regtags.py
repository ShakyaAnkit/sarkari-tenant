import datetime
import re

from pytz import timezone

from django import template
from django.utils.translation import ugettext, ungettext

register = template.Library()

@register.filter(name='int_nep')
def convertIntToNepali(eng_int):
    devanagari_nums = ('०', '१', '२', '३', '४', '५', '६', '७', '८', '९')
    number = str(int(eng_int))
    return ''.join(devanagari_nums[int(digit)] for digit in number)


@register.filter(name='timesince_nep')
def timesinceNep(date):
    #date = date.replace(tzinfo=None)
    nepalTZ = timezone('Asia/Kathmandu')

    nowTime = datetime.datetime.now()
    nowTime = nowTime.replace(tzinfo=nepalTZ)
    delta = nowTime - date

    num_years = delta.days // 365

    if (num_years > 0):
        return ungettext(u"%s वर्ष अघि", u"%s वर्ष अघि", num_years) % convertIntToNepali(num_years)

    num_weeks = delta.days // 7
    if (num_weeks > 0):
        return ungettext(u"%s हप्ता अघि", u"%s हप्ता अघि", num_weeks) % convertIntToNepali(num_weeks)

    if (delta.days > 0):
        return ungettext(u"%s दिन अघि", u"%s दिन अघि", delta.days) % convertIntToNepali(delta.days)

    num_hours = int(delta.seconds) // 3600
    if (num_hours > 0):
        return ungettext(u"%s घण्टा अघि", u"%s घण्टा अघि", num_hours) % convertIntToNepali(num_hours)

    num_minutes = delta.seconds // 60
    if (num_minutes > 0):
        return ungettext(u"%s मिनेट अघि", u"%s मिनेट अघि", num_minutes) % convertIntToNepali(num_minutes)

    return ugettext(u"केहि सेकेन्ड अघि")