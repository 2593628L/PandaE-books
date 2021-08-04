from django import forms
from django.forms.models import model_to_dict
from panda.models import Book, Category,UserProfile
from django.contrib.auth.models import User

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
    name = forms.CharField(max_length=50,help_text="please enter the category name")
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)
    rating = forms.FloatField(widget=forms.HiddenInput(),initial=0.0)
    description = forms.CharField(max_length=500,help_text="please enter the description ")
    class Meta:
        model = Book
        exclude=('category',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ( 'picture',)