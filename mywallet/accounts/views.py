from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm


def signup(request):
    template_name = 'signup.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, template_name, context)


def preferences(request):
    return render(request, 'preferences.html')