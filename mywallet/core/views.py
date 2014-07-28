from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mywallet.bills.models import Bill
from mywallet.bills.forms import BillForm
from mywallet.accounts.models import User


def index(request):
    return render(request, 'index.html')


@login_required
def home(request):
    user = request.user
    bills = Bill.objects.filter(user=user)
    form = BillForm(user)
    total = 0
    for bill in bills:
        if bill.bill_type == 'revenue':
            total += bill.value
        else:
            total -= bill.value

    context = {
        'form': form,
        'bills': bills,
        'total': total
    }

    return render(request, 'home.html', context)


def bill(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = BillForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()

    return redirect('core:home')
