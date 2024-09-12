from django import forms
from django_recaptcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ihr Name")
    email = forms.EmailField(label="Ihre E-Mail-Adresse")
    message = forms.CharField(widget=forms.Textarea, label="Nachricht")
    captcha = ReCaptchaField()