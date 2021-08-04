from panda.views import ProfileView
from django.urls import path
from panda import views

app_name = 'panda'

urlpatterns =[
    path('',views.homepage, name='homepage'),  
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    path('book/<slug:book_name_slug>',views.show_book, name='show_book'),
    path('add_category/',views.add_category,name="add_category"),
    path('register_profile/',views.register_profile,name="register_profile"),
    path('profile/<username>/',views.ProfileView.as_view(),name='profile'),
    path('category/<slug:category_name_slug>/add_book/', views.add_book, name='add_book'),
]