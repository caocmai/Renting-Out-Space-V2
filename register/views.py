from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.

class Test(CreateView):
    def get(self, request):
        return render(request, "register.html", {"test": "test"})