from django.db import models
from django.dispatch import receiver

# Create your models here.

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    sender_name = models.CharField(max_length=50,default='')
    sender_email = models.EmailField(max_length=100,default='')
    amount = models.IntegerField(default=0)
    receiver_name = models.CharField(max_length=50,default='')
    receiver_email = models.EmailField(max_length=100,default='')

    def __str__(self) :
        return self.sender_name
