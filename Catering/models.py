from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=20, blank=False)
    Last_Name = models.CharField(max_length=20, blank=False)
    City = models.CharField(max_length=40, blank=False)
    Phone = models.CharField(max_length=10, blank=False)
    Address = models.TextField()

    def __str__(self):
        return self.user.username


class Restaurant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Restaurant_Name = models.CharField(max_length=100, blank=False)
    Info = models.CharField(max_length=50, blank=False)
    Min_order = models.CharField(max_length=5, blank=False)
    Location = models.CharField(max_length=40, blank=False)
    Restaurant_Logo = models.ImageField(blank=False)

    REST_STATE_OPEN = "Open"
    REST_STATE_CLOSE = "Closed"
    REST_STATE_CHOICES = (
        (REST_STATE_OPEN, REST_STATE_OPEN),
        (REST_STATE_CLOSE, REST_STATE_CLOSE)
    )
    status = models.CharField(max_length=50, choices=REST_STATE_CHOICES, default=REST_STATE_OPEN, blank=False)
    approved = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.Restaurant_Name


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=30, blank=False)
    Category = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.First_Name


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    Item_Name = models.ForeignKey(Item, on_delete=models.CASCADE)
    Restaurant_Names = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Price = models.IntegerField(blank=False)
    Quantity = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.Item_Name.First_Name + ' - ' + str(self.Price)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    Total_amount = models.IntegerField(default=0)
    Timestamp = models.DateTimeField(auto_now_add=True)
    Delivery_Address = models.CharField(max_length=50, blank=True)
    OrderedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    Restaurant_Names = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    ORDER_STATE_WAITING = "Waiting"
    ORDER_STATE_PLACED = "Placed"
    ORDER_STATE_ACKNOWLEDGED = "Acknowledged"
    ORDER_STATE_COMPLETED = "Completed"
    ORDER_STATE_CANCELLED = "Cancelled"
    ORDER_STATE_DISPATCHED = "Dispatched"

    ORDER_STATE_CHOICES = (
        (ORDER_STATE_WAITING, ORDER_STATE_WAITING),
        (ORDER_STATE_PLACED, ORDER_STATE_PLACED),
        (ORDER_STATE_ACKNOWLEDGED, ORDER_STATE_ACKNOWLEDGED),
        (ORDER_STATE_COMPLETED, ORDER_STATE_COMPLETED),
        (ORDER_STATE_CANCELLED, ORDER_STATE_CANCELLED),
        (ORDER_STATE_DISPATCHED, ORDER_STATE_DISPATCHED)
    )
    status = models.CharField(max_length=50, choices=ORDER_STATE_CHOICES, default=ORDER_STATE_WAITING)

    def __str__(self):
        return str(self.id) + ' ' + self.status


class orderItem(models.Model):
    id = models.AutoField(primary_key=True)
    Item_Name = models.ForeignKey(Menu, on_delete=models.CASCADE)
    Order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class Feedback(models.Model):
    Customer_Name = models.CharField(max_length=20, blank=False)
    Email = models.EmailField()
    Product = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    Details = models.TextField()
    Happy = models.BooleanField()
    Sad = models.BooleanField()
    Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.Customer_Name)


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from" + self.name + '-' + self.email
