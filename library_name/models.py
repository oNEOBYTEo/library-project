from django.db import models

# Create your models here.

class Library(models.Model):
    name_library = models.CharField(max_length=50)
    addres_library = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name_library} | {self.addres_library}"
