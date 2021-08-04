from django.urls import path
from panda import views

app_name = 'panda'

urlpatterns =[
    path('',views.homepage, name='homepage'),  
]