from django.db import models
from mywallet.accounts.models import User


class Bill(models.Model):
    name = models.CharField('Name', max_length=200)
    value = models.DecimalField('Value', max_digits=8, decimal_places=2)
    bill_type = models.CharField('Type', max_length=8)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = 'Bills'
