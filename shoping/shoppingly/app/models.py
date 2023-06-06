from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.
STATE_CHOICES =(
('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Aruachal Pradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
)
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete =models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES,max_length=50)
    def __str__(self):
     return str(self.id)

CATEGORY_CHOICES = (
    ('M','mobile'),
    ('L','laptop'),
    ('TW','topwear'),
    ('BW','bottomwear'),
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand= models.CharField(max_length=100)
    category = models.CharField(choices = CATEGORY_CHOICES,max_length = 2)
    Product_image = models.ImageField(upload_to = 'productimg')
    def __str__(self):
     return str(self.id)
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.PositiveIntegerField(default = 1)
    def __str__(self):
        return str(self.id)
STATUS_CHOICES = (
    ('accepted','accepted'),
    ('packed','packed'),
    ('on the way','on the way'),
    ('delivered','delivered'),
    ('cancel','cancel')
)
class Orderplaced(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=50,choices = STATUS_CHOICES,default='pendinng')