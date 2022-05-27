from django.db import models

# Create your models here.
class Shelf(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Category: {self.category} | N°: {self.id}"
