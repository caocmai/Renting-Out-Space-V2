from django.urls import path
from register.views import Test, register


urlpatterns = [
    path('', Test.as_view(), name="test-view"),
    path('new/', register, name="sign-up-page"),

]
