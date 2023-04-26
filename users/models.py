 from django.db import models
 class Customer(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,primary_key=True)
    
    