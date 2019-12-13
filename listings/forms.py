from django import forms
from listings.models import Listing, Comment


class ListingForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Listing
        fields = ("title", "description", "link_to_image", "total_area", "price_per_month")
   
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content", )