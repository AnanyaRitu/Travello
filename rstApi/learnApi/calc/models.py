from django.db import models

# Create your models here.

class destination (models.Model) :  #(model.Model) makes sure it can convert the class into a model for database
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='img')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

