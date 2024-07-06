from django.db import models
from NumberCollection.models.model import BasicModel

class Number(BasicModel):
    class Meta:
        db_table = "numbers"

    number = models.DecimalField(max_digits=10, decimal_places=0)
    is_prime = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.username
        