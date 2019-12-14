from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from listings.models import Listing
from listings.forms import ListingForm
# Create your tests here.


class ListingTestCase(TestCase):

    # Test to sure the slug is created when a listing is created
    def test_page_slugify_on_save(self):
        user = User()
        user.save()

        listing = Listing(title="A New Listing", description="A short description", price_per_month=120, total_area=234.34, author=user)
        listing.save()

        self.assertEqual(listing.slug, 'a-new-listing')

class ListingViewTests(TestCase):
    
    # Test to one specific page when creating a listing
    def test_one_specific_page(self):
        user = User.objects.create() # This line will both create the user and save it
        listing = Listing(title="A New Listing", description="A short description", price_per_month=120, total_area=234.34, author=user)
        listing.save()

        response = self.client.get(reverse_lazy('listing-details-page', args=(listing.slug,)))

        self.assertEqual(response.status_code, 200)


class FormPostTest(TestCase):
    """ To test form creation """

    # Test to make sure the listing form is valid
    def test_form(self):

        form_info = {
            'title': "Test title",
            'description': "The description in here",
            'link_to_image': "www.theimage.com",
            'price_per_month': 120,
            'total_area': 123.23,
         }

        form = ListingForm(data=form_info)
        self.assertTrue(form.is_valid())