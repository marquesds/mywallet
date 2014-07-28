from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mywallet.bills.models import Bill


def index(request):
    return render(request, 'index.html')


@login_required
def home(request):
    user = request.user
    bills = Bill.objects.filter(user=user)
    total = 0
    for bill in bills:
        if bill.bill_type == 'revenue':
            total += bill.value
        else:
            total -= bill.value

    context = {
        'bills': bills,
        'total': total
    }

    return render(request, 'home.html', context)
