from django.urls import path
from panda import views

app_name = 'panda'

urlpatterns =[
    path('',views.homepage, name='homepage'),  
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    path('add_category/',views.add_category,name="add_category"),
    path('category/<slug:category_name_slug>/add_book/', views.add_book, name='add_book'),
]