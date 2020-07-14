from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.
class User(models.Model):
    Hospital_id = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    Address = models.CharField(max_length=500)
    Phone_Number = models.CharField(max_length=12)

    def __str__(self):
        return self.Hospital_id + "-" + self.Firstname

class Document(models.Model):
    Hospital_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Document_type = models.CharField(max_length=20)
    Document_image = models.FileField()

    def get_absolute_url(self):
        return reverse('first:detail', kwargs={'pk':self.pk})


