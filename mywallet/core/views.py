from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mywallet.bills.models import Bill
from mywallet.bills.forms import BillForm
from mywallet.accounts.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

    # Django pagination
    paginator = Paginator(bills, 5)
    page = request.GET.get('page')
    try:
        bills = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        bills = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        bills = paginator.page(paginator.num_pages)

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
