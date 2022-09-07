from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)
class Person(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, default='GENDER', max_length=10, null=False, blank=False)
    
class RateLimit(models.Model):
    count = models.IntegerField()
    user = models.CharField(max_length=50, null=False, blank=False)