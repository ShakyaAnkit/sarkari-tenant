import re
import nepalicalendar
import dateutil.parser

from django import template
from datetime import timedelta, date, datetime

register = template.Library()


@register.filter(name='int_nep')
def convertIntToNepali(eng_int):
    devanagari_nums = ('०', '१', '२', '३', '४', '५', '६', '७', '८', '९')
    number = str(int(eng_int))
    return ''.join(devanagari_nums[int(digit)] for digit in number)

#English date to Nepali
@register.filter(name='date_to_nep')
def dateInToNepali(dateStr):
    if type(dateStr) == date:
        dateStr = datetime(dateStr.year, dateStr.month, dateStr.day)
    try:
        dt = dateStr + timedelta(hours=5,minutes=45,seconds=0)
        datetime_date = dateutil.parser.parse(str(dt))
        day_words = datetime_date.strftime('%A')
        npdt = nepalicalendar.nepdate.NepDate.from_ad_date(dateStr.date())
        year = npdt.year
        month = npdt.month
        day = npdt.day
        dayArrEng = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4,
                     'Thursday': 5, 'Friday': 6, 'Saturday': 7}
        monthArr = ['बैशाख', 'जेठ', 'असार', 'साउन', 'भदौ', 'असोज',
                    'कात्तिक', 'मंसिर', 'पुस', 'माघ', 'फागुन', 'चैत']
        toRetYear = convertIntToNepali(int(year))
        toRetMonth = monthArr[int(month) - 1]
        toRetDay = convertIntToNepali(day)
        return toRetMonth + ' ' + toRetDay + ', ' + toRetYear 
    except:
        return dateStr

#Nepali Month 
@register.filter(name='nep_month')
def dateInToNepaliMonth(dateStr):
    try:
        dt = dateStr + timedelta(hours=5,minutes=45,seconds=0)
        datetime_date = dateutil.parser.parse(str(dt))
        npdt = nepalicalendar.nepdate.NepDate.from_ad_date(datetime_date.date())
        month = npdt.month
        monthArr = ['बैशाख', 'जेठ', 'असार', 'साउन', 'भदौ', 'असोज',
                    'कात्तिक', 'मंसिर', 'पुस', 'माघ', 'फागुन', 'चैत']
        toRetMonth = monthArr[int(month) - 1]
        return toRetMonth
    except:
        return dateStr

#Nepali Date
@register.filter(name='nep_date')
def dateInToNepaliDate(dateStr):
    try:
        dt = dateStr + timedelta(hours=5,minutes=45,seconds=0)
        datetime_date = dateutil.parser.parse(str(dt))
        npdt = nepalicalendar.nepdate.NepDate.from_ad_date(datetime_date.date())
        day = npdt.day
        toRetDay = convertIntToNepali(day)
        return toRetDay
    except:
        return dateStr
