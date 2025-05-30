from django.forms import ModelForm
from .models import Page

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'body', 'page_date']
