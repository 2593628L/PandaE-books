from typing import Coroutine
from django.forms import models
from panda.models import UserProfile,Post
from panda.forms import CategoryForm,BookForm,UserProfileForm
from panda.models import Category,Book,Comments
from django.http.response import HttpResponse 
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from panda.bing_search import run_query

# Create your views here.

def homepage(request):
    context_dict ={}
    all_category = Category.objects.order_by('-likes')
    category_list = Category.objects.order_by('-likes')[:5]
    book_list = Book.objects.order_by('-likes')[:5]
    context_dict['all_category'] = all_category
    context_dict['categories'] = category_list
    context_dict['books'] = book_list
    return render(request,'panda/homepage.html',context=context_dict)

def show_category(request,category_name_slug):
    context_dict={}
    try:
        category = Category.objects.get(slug=category_name_slug)
        books = Book.objects.filter(category=category)
        context_dict['books'] = books
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['books'] = None
    return render(request, 'panda/category.html', context=context_dict)

def show_book(request,book_name_slug):
    context_dict={}
    try:
        book = Book.objects.get(slug=book_name_slug)
        context_dict['book'] = book
        if request.method == 'POST':
            content = request.POST['content']
            comments = Comments(content=content,)
            comments.save()
    except Book.DoesNotExist:

        context_dict['book'] = None
    return render(request, 'panda/book.html', context=context_dict)
@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect(reverse('panda:homepage'))
        else:
            print(form.errors)
    context_dict = {'form':form}
    return render(request,'panda/profile_registration.html',context_dict)



def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('homepage')
    return render(request, 'panda/addCategory.html',{'form':form})

def add_book(request, category_name_slug):
    try:
        
        category = Category.objects.get(slug=category_name_slug)
    except:
        category = None
   
    # You cannot add a page to a Category that does not exist... DM
    if category is None:
        return redirect(reverse('panda:homepage'))
    
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            if category:
                book = form.save(commit=False)
                book.category = category
                book.views = 0
                book.save()
                return redirect(reverse('panda:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)  # This could be better done; for the purposes of TwD, this is fine. DM.
    
    context_dict = {'form': form, 'category': category}
    return render(request, 'panda/add_book.html', context=context_dict)

class ProfileView(View):
        def get_user_details(self,username):
            try :
                user =User.objects.get(username=username)
            except User.DoesNotExist:
                return None
            user_profile = UserProfile.objects.get_or_create(user=user)[0]
            form = UserProfileForm({'image':user_profile.picture})

            return (user, user_profile, form) 
        
        @method_decorator(login_required)
        def get(self, request, username):
            try:
                (user, user_profile,form) = self.get_user_details(username)
            except TypeError:
                return redirect(reverse('panda:homepage'))
            context_dict = {'user_profile':user_profile,
                            'selected_user':user,
                            'form':form}
            return render(request,'panda/profile.html',context_dict)
        
        @method_decorator(login_required)
        def post(self,request,username):
            try:
                (user,user_profile,form) = self.get_user_details(username)
            except TypeError:
                return redirect(reverse('panda:homepage'))
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save(commit=True)
                return redirect('panda:profile',user.username)
            else:
                print(form.errors)
            context_dict = {'user_profile':user_profile,
                            'selected_user':user,
                            'form':form}
            return render(request,'panda/profile.html',context_dict)


def search(request):
    q = request.GET.get('q')
    error_msg = ''
    context_dict ={}
    try:
        book = Book.objects.get(name=q)
        context_dict['book'] = book
        return render(request, 'panda/book.html', context=context_dict)
    except Category.DoesNotExist:
        return render(request, 'panda:homepage')
    