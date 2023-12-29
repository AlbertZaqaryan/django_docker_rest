from django.db import models

# Create your models here.

class Car(models.Model):

    model = models.CharField('Car model', max_length=60)
    price = models.PositiveIntegerField('Car price')

    def __str__(self):
        return self.model
    
class Book(models.Model):
    
    name = models.CharField("Book name", max_length = 60)
    page = models.PositiveBigIntegerField("Book pages")
    image = models.ImageField("Book image", upload_to='book')

    def __str__(self) -> str:
        return self.name
    

class Film(models.Model):

    name = models.CharField("Film name", max_length = 60)
    lenghth = models.PositiveIntegerField("Film length")

    def __str__(self) -> str:
        return self.name
    

class Notebook(models.Model):

    name = models.CharField("Notebook name", max_length = 60)
    model = models.CharField("Notebook model", max_length = 60)

    def __str__(self) -> str:
        return self.name