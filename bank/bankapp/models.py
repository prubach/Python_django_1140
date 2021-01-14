from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField('Birth Date')

    def __str__(self):
        return 'Customer[ %s, %s, %s]' % (self.first_name, self.last_name, self.email)


class Account(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return 'Account[ %s, %s, %s]' % (self.customer.last_name, self.type, self.balance)
