from django.db import models
from Persons.models import Person

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return title

