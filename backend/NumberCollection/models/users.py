import uuid
from django.db import models

class User(models.Model):
    class Meta:
        db_table = "users"


    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    uuid = models.UUIDField(editable=False, unique=True, auto_created=True, default=uuid.uuid4)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
        