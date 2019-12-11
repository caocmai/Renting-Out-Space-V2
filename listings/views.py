from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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
          'pages': listings
        })

class ListingCreateView(CreateView):

  form_class = ListingForm
  # success_url = reverse_lazy('list.html')
  template_name = "new_listing.html"

  # def get(self, request, *args, **kwargs):
  #   context = {'form': PageForm()}
  #   return render(request, 'new_wiki.html', context)

  # args and kwards in not needed for this to work
  def post(self, request, *args, **kwargs):
      form = ListingForm(request.POST)
      if form.is_valid():
          wiki = form.save()
          wiki.save()
          return HttpResponseRedirect(reverse_lazy('listing-details-page', args=[wiki.slug]))


class ListingDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Listing

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        listing = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': listing
        })