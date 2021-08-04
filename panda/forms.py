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
    slug = forms.SlugField(widget=forms.HiddenInput(),required=False)
    views = forms.IntegerField(default=0)
    image = forms.ImageField(verbose_name=name,upload_to='book_images',blank = True)
    likes = forms.IntegerField(default=0)
    rating = forms.FloatField(default=0.0)
    description = forms.CharField(max_length=500)