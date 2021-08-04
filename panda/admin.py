from django.contrib import admin
from panda.models import Category,Book,UserProfile,Comments,Favorites

# Register your models here.
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Book)
admin.site.register(Favorites)
admin.site.register(UserProfile)


