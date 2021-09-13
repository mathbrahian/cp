from django.db import models
from Country.models import Country

class Person(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return name
