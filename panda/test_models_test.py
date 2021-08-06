from panda.models import Category
from django.test import TestCase
class CategoryMethodTests(TestCase): # Test Models
    def test_ensure_likes_are_positive(self):
            category = Category(name = 'test', likes=-1)
            category.save()

            self.assertEqual((category.likes >= 0), True)
    
    def test_slug_lint_creation(self):
        category = Category(name = 'Panda E books')
        category.save()

        self.assertEqual(category.slug, 'panda-e-books')

