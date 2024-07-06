from django.db import models
from NumberCollection.models.users import User
from NumberCollection.models.numbers import Number
from NumberCollection.models.model import BasicModel

class UserNumberRelations(BasicModel):
    class Meta:
        db_table = "user_number_relations"

    number_id = models.ForeignKey(Number, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user_id} - {self.number_id}'
        