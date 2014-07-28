from django import forms
from .models import Bill


class BillForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        bill = super(BillForm, self).save(commit=False)
        if commit:
            bill.save()
        return bill

    class Meta:
        model = Bill
        fields = ['name', 'value', 'bill_type']
