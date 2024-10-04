from django import forms
from django_recaptcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(max_length=100, label="Email")
    phone = forms.CharField(max_length=100, label="Phone")
    subject = forms.CharField(max_length=250, label="Subject")
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()