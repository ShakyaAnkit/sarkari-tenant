from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from django import forms

from dashboard.models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['deleted_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'captcha':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

    def clean(self):
        cleaned_data = super(MessageForm, self).clean()
        phone_no = cleaned_data.get('phone_no')

        if phone_no:
            if not len(str(phone_no)) in range(7, 14):
                raise forms.ValidationError({'phone_no': ['Please Enter a Valid Phone Number ']})