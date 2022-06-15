from django import forms
from django.forms import inlineformset_factory
from documents.models import Quote, QuoteItem

class QuoteItemForm(forms.ModelForm):
    class Meta:
        model = QuoteItem
        fields = '__all__'
    

class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = '__all__'
