from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView, DeleteView, CreateView

from listings.models import Listing
from listings.forms import ListingForm
# Create your views here.

class ListingsListView(ListView):
    """ Renders a list of all Pages. """
    model = Listing

    def get(self, request):
        """ GET a list of Pages. """
        listings = self.get_queryset().all()
        return render(request, 'listings/listings.html', {
          'listings': listings
        })

class ListingCreateView(CreateView):

  form_class = ListingForm
  # success_url = reverse_lazy('list.html')
  template_name = 'listings/new_listing.html'

  # args and kwards in not needed for this to work
  def post(self, request, *args, **kwargs):
      form = ListingForm(request.POST)
      if form.is_valid():
          listing = form.save()
          listing.save()
          return HttpResponseRedirect(reverse_lazy('listing-details-page', args=[listing.slug]))


class ListingDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Listing


    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        listing = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'listings/single_listing.html', {
          'listing': listing
        })

class ListingUpdateView(UpdateView):
  model  = Listing
  fields = ['title', 'description', 'link_to_image', 'price_per_month', 'total_area']
  template_name = 'listings/new_listing.html'

class ListingDeleteView(DeleteView):
  model = Listing
  success_url = reverse_lazy('listing-list-page')
  template_name = 'listings/delete_listing.html'