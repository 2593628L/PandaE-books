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

