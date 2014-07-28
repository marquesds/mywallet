from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from mywallet.accounts.models import User

@login_required
def home(request):
    user = get_object_or_404(User)
    context = {
        'user': user
    }
    return render(request, 'index.html', context)
