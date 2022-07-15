from django.db import models

# Create your models here.
class Cart(models.Model):
    itemName=models.CharField(max_length=100)
    quantity=models.IntegerField()
    date=models.DateField()
    
    def __str__(self):
        return self.itemName