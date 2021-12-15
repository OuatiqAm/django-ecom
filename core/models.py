import string
import random
from io import BytesIO

from PIL.Image import Image
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files import File
from django.db import models


# Create your models here.

ORDER_CHOICES =(("O","OPEN"),("A","ARCHIVED"),("C","CANCELED"))


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    customer_id = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "customer"


class Category(models.Model):
    name = models.CharField(max_length=20, default='')
    slug = models.SlugField(default="")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name_plural = "categories"

class Item(models.Model):
    name = models.CharField(max_length=20, default='')
    slug = models.SlugField(default="")
    sku = models.CharField(max_length= 12, default='')
    description = models.TextField( blank=True, null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='upload/', blank=True, null=True)

    category = models.ForeignKey(Category,on_delete = models.CASCADE, blank=True, null=True)

    def get_cat(self):
        return  self.category

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return "http://127.0.0.1:8000" + self.thumbnail.url
        else:
            if self.image:
                 self.thumbnail = self.make_thumbail(self.image)
                 self.save()
                 return "http://127.0.0.1:8000" + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self,image, size=(300,250)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbail(size)

        thumb_io = BytesIO()
        img.save(thumb_io,'JPEG',quality=80)
        thumbnail = File(thumb_io, name= image.name)

        return  thumbnail

    class Meta:
        db_table = "item"


class Order(models.Model):
    creation_date = models.DateTimeField(null=True)
    close_date = models.DateTimeField(null=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    status = models.CharField(choices= ORDER_CHOICES, max_length=2,null=True)
    reference = models.CharField(max_length=12, default='')

    user = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)

    class Meta:
        db_table = "orders"

class OrderItems(models.Model):
    item = models.ForeignKey(Item, on_delete= models.DO_NOTHING,  blank=True, null=True)
    order  = models.ForeignKey(Order,on_delete=models.DO_NOTHING,  blank=True, null=True)
    quantity = models.IntegerField(default=0)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=True)

    class Meta:
        db_table = "order_item"

class Payment(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    payment_date_time = models.DateTimeField(null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,  blank=True, null=True)

    class Meta:
        db_table = "payment"

class Address(models.Model):
    street_address = models.CharField(max_length=120, default="")
    apartment_address = models.CharField(max_length=120,  default="")
    zip = models.CharField(max_length=10,  default="")
    default = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)

    class Meta:
        db_table = "address"


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_letters +'0123456789'
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)