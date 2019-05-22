from django.db import models

class MySimpleModel(models.Model):
    col = models.CharField(max_length=10)

class Stocks(models.Model):
    date = models.DateField(auto_now=True)
    predicted_buying_power = models.DecimalField(max_digits=10, decimal_places=2)
    new_portfolio = models.CharField(max_length=150)

    future_portfolio = models.CharField(max_length=150, default=None)
    future_price = models.CharField(max_length=150, default=None)
    buying_power = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    future_buying_power = models.DecimalField(max_digits=10, decimal_places=2, default=None)