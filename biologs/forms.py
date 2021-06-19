from django import forms
from .models import BiologPost

class BiopostForm(forms.ModelForm):
    """ Biopost posting form. """
    class Meta:
        model = BiologPost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Text'}
