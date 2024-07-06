from django.db import models
from NumberCollection.models.model import BasicModel

class Number(BasicModel):
    class Meta:
        db_table = "numbers"

    # tipo bigint
    number = models.BigIntegerField(blank=False, null=False)
    is_prime = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.number
    
    # checa se é primo antes de salvar
    def save(self, *args, **kwargs):
        self.is_prime = self.is_prime_number()
        super(Number, self).save(*args, **kwargs)


    # OTIMIZAR
    def is_prime_number(self):
        if self.number <= 1:
            return False
        if self.number <= 3:
            return True
        if self.number % 2 == 0 or self.number % 3 == 0:
            return False
        i = 5
        while i * i <= self.number:
            if self.number % i == 0 or self.number % (i + 2) == 0:
                return False
            i += 6
        return True
        