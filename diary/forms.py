from django.forms import ModelForm
from .models import Page
from django.forms.widgets import DateInput

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'body', 'page_date']
        widgets = {
            'page_date': DateInput(attrs={'type': 'date'})
        }