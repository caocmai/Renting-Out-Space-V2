from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView, DeleteView, CreateView

from listings.models import Listing, Comment
from listings.forms import ListingForm, CommentForm
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
        listing = form.save(commit=False)
        listing.author = request.user
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
  """Update listing"""
  model  = Listing
  fields = ['title', 'description', 'link_to_image', 'price_per_month', 'total_area']
  template_name = 'listings/new_listing.html'

class ListingDeleteView(DeleteView):
  """Delete a listing"""
  model = Listing
  success_url = reverse_lazy('listing-list-page')
  template_name = 'listings/delete_listing.html'

class CommentCreateView(CreateView):
  """To creat a comment"""
  form_class = CommentForm
  success_url = reverse_lazy('/')

  template_name = 'listings/new_comment.html'

  # args and kwards in not needed for this to work
  # def post(self, request, *args, **kwargs):
  #     form = CommentForm(request.POST)
  #     if form.is_valid():
  #         form = form.save()
  #         form.save()
  #         return HttpResponseRedirect(reverse_lazy('listing-details-page', args=[form.slug]))

# 
def add_comment_to_post(request, slug):
    """Add comment to a post"""
    listing = get_object_or_404(Listing, slug=slug)
    # post = Listing.objects.get(slug=slug)
    form = CommentForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
          comment = form.save(commit=False)
          # Need to do this for all forgien keys!!!!!
          comment.username = request.user
          comment.listing = listing
          comment.save()
          return redirect('listing-details-page', slug=listing.slug)
    else:
        form = CommentForm()
    return render(request, 'listings/new_comment.html', {'form': form, 'listing': listing})