from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "E1/index.html"
class AboutView(TemplateView):
    template_name = "E1/about.html"
class ContactsView(TemplateView):
    template_name = "E1/contacts.html"
