from django.urls import path
from listings.views import ListingsListView, ListingCreateView, ListingDetailView, ListingUpdateView, ListingDeleteView


urlpatterns = [
    path('', ListingsListView.as_view(), name='listing-list-page'),
    path('new_listing/', ListingCreateView.as_view(), name='listing-create-page'),
    path('update_listing/<str:slug>/', ListingUpdateView.as_view(), name='listing-update-page'),
    path('delete_listing/<str:slug>/', ListingDeleteView.as_view(), name='listing-delete-page'),
    path('<str:slug>/', ListingDetailView.as_view(), name='listing-details-page'),
]