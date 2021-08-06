import os
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings
from panda.models import Category
from django.test import TestCase

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


class HomepageTest(TestCase):
    # """
    # Testing the basics of your index view and URL mapping.
    # Also runs tests to check the response from the server.
    # """
    def setUp(self):
        self.views_module = importlib.import_module('panda.views')
        self.views_module_listing = dir(self.views_module)
        
        self.project_urls_module = importlib.import_module('panda_ebooks.urls')
    
    def test_view_exists(self):
        """
        Does the homepage() view exist in panda's views.py module?
        """
        name_exists = 'homepage' in self.views_module_listing
        is_callable = callable(self.views_module.homepage)
        
        self.assertTrue(name_exists, f"The homepage view for panda does not exist.")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check that you have created the homepage() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
    
    def test_mappings_exists(self):
        """
        Are the two required URL mappings present and correct?
        One should be in the project's urls.py, the second in panda's urls.py.
        """
        index_mapping_exists = False
        
        # This is overridden. We need to manually check it exists.
        for mapping in self.project_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'homepage':
                    index_mapping_exists = True
        
        self.assertTrue(index_mapping_exists, f"{FAILURE_HEADER}The index URL mapping could not be found. Check your PROJECT'S urls.py module.{FAILURE_FOOTER}")

