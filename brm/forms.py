from django import forms

class NewBookForm(forms.Form):
    title=forms.CharField(label='Title',max_length=100)
    author=forms.CharField(label='Author',max_length=100)
    price=forms.FloatField(label='Price')
    publisher=forms.CharField(label='publisher')
class SearchForm(forms.Form):
    title=forms.CharField(label='Title',max_length=100)
