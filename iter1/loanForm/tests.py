from django.test import TestCase
from django import forms
from .forms import *
from loanForm.models import *

# Create your tests here.

class ProductTestCase(TestCase):

    def test_empty(self):
        form = ProductForm(data={'name': ''})
        self.assertFalse(form.is_valid())

    def test_valid(self):
        form = ProductForm(data={'name': 'Jon', 'amount': 10000,
                                'type': 'oth', 'years': 3})
        self.assertTrue(form.is_valid())

    def test_invalid(self):
        form = ProductForm(data={'name': 'Dan', 'amount': "",
                                'type': "oth", 'years': 30})
        self.assertFalse(form.is_valid())
