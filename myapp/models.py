from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, default='Furniture')
    warehouse = models.CharField(max_length=200, default='Windsor')

    def __str__(self):
        return self.name


class Product(models.Model):
    interested = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='TV')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100, validators=[MaxValueValidator(1000), MinValueValidator(0)])
    available = models.BooleanField(default=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
    def refill(self):
        self.stock=self.stock+100

class Client(User):
    PROVINCE_CHOICES = [
        ('AB', 'Alberta'),
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec'),
    ]

    company = models.CharField(max_length=50, blank=True, default='NN')
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    interested_in = models.ManyToManyField(Category)

    def __str__(self):
        return self.company


class Order(models.Model):
    ORDER_CHOICES = [
        (0, 'Order Cancelled'),
        (1, 'Order Placed'),
        (2, 'Order Shipped'),
        (3, 'Order Delivered')
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    num_units = models.PositiveIntegerField(default=1)
    order_status = models.IntegerField(choices=ORDER_CHOICES, default=1)
    status_date = models.DateField(auto_now=True)

    def __str__(self):
        #return "Client:" + str(self.client) + "  Date:" + str(self.status_date)
        return self.product
    def total_cost(self):
        return self.product.price * self. num_units