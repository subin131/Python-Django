from tkinter import CASCADE
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.IntegerField()
    
    
    def __str__(self):
        return self.first_name+" "+self.last_name
    
    
class Citizen(models.Model):
    ctznumber=models.IntegerField(primary_key=True)
    place=models.CharField(max_length=30)
    date=models.DateField()
    user=models.OneToOneField(Person,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.ctznumber)