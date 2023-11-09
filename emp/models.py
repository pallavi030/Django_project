from django.db import models

# Create your models here.
class Emp(models.Model):
    # name=models.CharField(max_length=200)
    email_id=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    # role=models.CharField(max_length=150)
    # working=models.BooleanField(default=True)

class Details(models.Model):
    name=models.CharField(max_length=200)
    email_id=models.CharField(max_length=100)
    password=models.CharField(max_length=15)
    confirm_password=models.CharField(max_length=15)
    role=models.CharField(max_length=150)


    