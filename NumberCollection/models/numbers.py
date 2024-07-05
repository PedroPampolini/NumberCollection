import uuid
from django.db import models

class Number(models.Model):
    class Meta:
        db_table = "numbers"


    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    uuid = models.UUIDField(editable=False, unique=True, auto_created=True, default=uuid.uuid4)
    number = models.DecimalField(max_digits=10, decimal_places=0)
    is_prime = models.BooleanField(blank=True, null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
        