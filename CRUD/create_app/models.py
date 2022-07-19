from django.db import models

# Create your models here.
class Create(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    
    def __str__(self):
        return self.first_name