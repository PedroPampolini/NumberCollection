from django.db import models
from NumberCollection.models.model import BasicModel

class User(BasicModel):
    class Meta:
        db_table = "users"

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
        