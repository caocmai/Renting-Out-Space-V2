from django.contrib import admin
from listings.models import Listing, Comment

# Register your models here.
admin.site.register(Listing)
admin.site.register(Comment)