from django.db import models

# Create your models here.
class Seller(models.Model):
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  profile =models.TextField(blank=True)
  
  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  seller= models.ForeignKey(Seller,on_delete=models.DO_NOTHING)
  def __str__(self):
    return self.name
