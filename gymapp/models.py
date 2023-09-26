from django.db import models
from django.utils import timezone

# Create your models here.
 
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=5)
    age = models.IntegerField( )
    purpose = models.CharField(max_length=50)
    membership_plan = models.CharField(max_length=100)
    total_fees = models.IntegerField()
    fees_paid = models.IntegerField()
    fees_remaining = models.IntegerField()
    last_paid_date = models.DateField()
    fees_due_date = models.DateField()
    date_of_join = models.DateField()
    updated_plan_date = models.DateField(default=timezone.now())
    personal_trainer = models.BooleanField(default=False)
    batch_time = models.CharField(max_length=50, default='Morning')
    personal_trainer_name = models.CharField(max_length=50, default='Not Applicable')

class Fee(models.Model):
    membership_plan_type = models.CharField(max_length=100)
    fee = models.IntegerField(default=0)
    pt_fee = models.IntegerField(default=0)


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    date_of_join = models.DateField(default=timezone.now())
    date_of_birth = models.DateField(default=timezone.now())
    gender = models.CharField(max_length=5, default=None)
    age = models.IntegerField(default=0)
