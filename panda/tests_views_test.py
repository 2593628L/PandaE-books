from django.http import response
from django.template.defaultfilters import length
from panda.models import Category
from django.test import TestCase
from django.urls import reverse
class IndexViewTests(TestCase):
    def test_homepage_view_with_no_categories(self):
        response = self.client.get(reverse('panda:homepage'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There is no ')
        self.assertQuerysetEqual(response.context['categories'], [])
    
    def test_homepage_view_with_categories(self):
        add_category('Art', 10)
        add_category('Computer', 20)
        add_category('History', 30)
        add_category('Fiction', 40)

        response = self.client.get(reverse('panda:homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Art")
        self.assertContains(response, "Computer")
        self.assertContains(response, "History")
        self.assertContains(response, "Fiction")

        length_of_categories = len(response.context['categories'])
        self.assertEquals(length_of_categories, 4)


#This is a helper function        
def add_category(name, likes = 10000):
    category = Category.objects.get_or_create(name=name)[0]
    category.likes = likes

    category.save()
    return category