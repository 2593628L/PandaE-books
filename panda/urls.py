from django.urls import path
from panda import views

app_name = 'panda'

urlpatterns =[
    path('',views.homepage, name='homepage'),  
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
]