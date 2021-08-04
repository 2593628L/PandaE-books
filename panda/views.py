from panda.models import Category,Book
from django.http.response import HttpResponse
from django.shortcuts import render

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