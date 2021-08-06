import os
import warnings
import importlib
from panda.models import Category, Book
from django.urls import reverse
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"
class AdminInterfaceTests(TestCase):

    def setUp(self):
        """
        Create a superuser account for use in testing.
        Logs the superuser in, too!
        """
        User.objects.create_superuser('testAdmin', 'email@email.com', 'adminPassword123')
        self.client.login(username='testAdmin', password='adminPassword123')
        
        category = Category.objects.get_or_create(name='TestCategory')[0]
        
    
    def test_admin_interface_accessible(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200, f"{FAILURE_HEADER}The admin interface is not accessible. Check that you didn't delete the 'admin/' URL pattern in your project's urls.py module.{FAILURE_FOOTER}")
    
    def test_models_present(self):
        """
        Checks whether the two models are present within the admin interface homepage
        """
        response = self.client.get('/admin/')
        response_body = response.content.decode()
        
        # Is the Panda app present in the admin interface's homepage?
        self.assertTrue('Models in the Panda application' in response_body, f"{FAILURE_HEADER}The Panda app wasn't listed on the admin interface's homepage. You haven't added the models to the admin interface.{FAILURE_FOOTER}")
        
        # Check each model is present.
        self.assertTrue('Categories' in response_body, f"{FAILURE_HEADER}The Category model was not found in the admin interface. If you did add the model to admin.py, did you add the correct plural spelling (Categories)?{FAILURE_FOOTER}")
        self.assertTrue('Books' in response_body, f"{FAILURE_HEADER}The Page model was not found in the admin interface. If you did add the model to admin.py, did you add the correct plural spelling (Books)?{FAILURE_FOOTER}")
    
       
