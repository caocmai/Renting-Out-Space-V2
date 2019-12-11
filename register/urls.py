from django.urls import path
from register.views import Test


urlpatterns = [
    path('', Test.as_view(), name="sign-up-view"),
]
