from panda.models import UserProfile
from panda.forms import CategoryForm,BookForm,UserProfileForm
from panda.models import Category,Book
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    context_dict ={}
    category_list = Category.objects.order_by('-likes')[:5]
    book_list = Book.objects.order_by('-likes')[:5]
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

def profile(request):
    return 

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

    # def register_profile(request):
    # form = UserProfileForm()
    # if request.method == 'POST':
    #     form = UserProfileForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         user_profile = form.save(commit=False)
    #         user_profile.user = request.user
    #         user_profile.save()

    #         return redirect(reverse('panda:homepage'))
    #     else:
    #         print(form.errors)
    # context_dict = {'form':form}
    # return render(request,'panda/profile_registration.html',context_dict)