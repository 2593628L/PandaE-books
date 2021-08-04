from django import forms
from django.forms.models import model_to_dict
from panda.models import Book, Category

class CategoryForm(forms.ModelForm):
    MAX_LENGTH = 200
    name = forms.CharField(max_length=MAX_LENGTH,help_text="please enter the category name")
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    Sdescription =forms.CharField(max_length=MAX_LENGTH,help_text="please enter the description of this category")
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = Category
        fields = ('name',)

class BookForm(forms.ModelForm):
    TITLE_MAX_SIZE = 128
    name = forms.CharField(max_length=TITLE_MAX_SIZE,help_text="please enter the book name")
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    # image = forms.ImageField()
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    rating = forms.FloatField(widget=forms.HiddenInput(),initial=0.0)
    description = forms.CharField(max_length=200,help_text="please enter the description")

    class Meta:
        model = Book
        exclude=('category',)