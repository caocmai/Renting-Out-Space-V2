from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from register.forms import UserRegistrationForm

class FormCreationTest(TestCase):
    """ To test form creation """

    def test_form(self):

        form_info = {
            'username': "johndoe",
            'email': "test@testing.com",
            'password1': "learncode",
            'password2': "learncode",
         }

        form = UserRegistrationForm(data=form_info)
        self.assertTrue(form.is_valid())
