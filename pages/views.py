from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = "home.html"
    
class ProjectsView(TemplateView):
    template_name = "projects.html"
    
class ServicesView(TemplateView):
    template_name = "services.html"

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('success_page')

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        subject_line = f'{subject} - von {name}'
        message = f'Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\nMessage:\n{message}'
        recipient_list = ['kd@duewiger.com']
        
        email = EmailMessage(
            subject_line,
            message,
            # use own mail and smtp-server to prevent spam filter or blocking
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            headers={'Reply-To': email},
        )
        email.send(fail_silently=False)
        
        return super().form_valid(form)
    
    
class ImprintView(TemplateView):
    template_name = "imprint.html"
    

class PrivacyView(TemplateView):
    template_name = "privacy.html"
    
class SuccessView(TemplateView):
    template_name = "success_page.html"