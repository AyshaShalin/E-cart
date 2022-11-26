from distutils.command.upload import upload
from django.db import models
from common.models import Seller
from ecom_admin.models import Category

# Create your models here.
class Product(models.Model):
    p_name = models.CharField(max_length = 20)
    seller = models.ForeignKey (Seller,on_delete=models.CASCADE)
    category =  models.ForeignKey (Category,on_delete=models.CASCADE ,default='')
    p_number = models.BigIntegerField()
    p_details = models.CharField(max_length = 600)
    p_price = models.BigIntegerField()
    p_stock = models.BigIntegerField()
    p_image = models.ImageField(upload_to='product/')