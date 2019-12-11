from django.shortcuts import render, redirect
from django.contrib import messages
from register.forms import UserRegistrationForm
from django.views.generic import CreateView

# Create your views here.

class Test(CreateView):
    def get(self, request):
        return render(request, "register/register.html", {"test": "test"})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register/register.html', {'form': form})