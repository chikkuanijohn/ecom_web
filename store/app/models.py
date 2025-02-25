from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
     cat_name=models.TextField()
     cat_image=models.FileField()

class Product(models.Model):
     pid=models.TextField()
     name=models.TextField()
     disc=models.TextField()
     img=models.FileField()
     cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)

class Weight(models.Model):
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     price=models.IntegerField()
     offer_price=models.IntegerField()
     product_weight=models.TextField()
     stock=models.IntegerField()

class Cart(models.Model):
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     weight=models.ForeignKey(Weight,on_delete=models.CASCADE)
     qty=models.IntegerField()

class Buy(models.Model):
    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('online', 'Online Payment'),
    ]
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    weight=models.ForeignKey(Weight,on_delete=models.CASCADE)
    qty=models.IntegerField()
    total_price=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='cod')
    billing_address = models.TextField(blank=True, null=True)




class Order(models.Model):
    STATUS_CHOICES = [
        ('Ordered', 'Ordered'),
        ('Shipped', 'Shipped'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    ]

    product = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    billing_address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Ordered')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.product} - {self.status}"

class Booking(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    weight = models.ForeignKey('Weight', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    billing_address = models.TextField()
    tracking_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=50, default="Pending")
    estimated_delivery = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - {self.product.name}"