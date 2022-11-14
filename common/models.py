from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Customer (models.Model) :
    c_firstname      = models.CharField(max_length = 20)
    c_secondname     = models.CharField(max_length = 20)
    c_email          = models.CharField(max_length = 60)
    c_number         = models.BigIntegerField()
    c_address        = models.CharField(max_length = 100)
    c_password       = models.CharField(max_length = 8)


class Seller (models.Model) :
    s_firstname     = models.CharField(max_length = 20)
    s_secondname    = models.CharField(max_length = 20)
    s_email         = models.CharField(max_length = 70)
    s_number        = models.BigIntegerField()
    s_address       = models.CharField(max_length = 100)
    s_accountnumber = models.BigIntegerField()
    s_ifsc          = models.CharField(max_length = 20)
    s_accholder     = models.CharField(max_length= 40)
    s_password      = models.CharField(max_length= 8)
    s_image         = models.ImageField(upload_to = 'seller/')