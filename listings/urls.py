from django.urls import path
from listings.views import ListingsListView, ListingCreateView, ListingDetailView


urlpatterns = [
    path('', ListingsListView.as_view(), name='listing-list-page'),
    path('new_listing', ListingCreateView.as_view(), name='listing-create-view'),
    path('<str:slug>/', ListingDetailView.as_view(), name='listing-details-page'),
]