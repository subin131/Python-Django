from django.db import models

# Create your models here.
class FormData(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.firstname