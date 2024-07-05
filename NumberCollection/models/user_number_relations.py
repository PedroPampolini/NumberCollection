import uuid
from django.db import models
from NumberCollection.models.users import User
from NumberCollection.models.numbers import Number

class UserNumberRelations(models.Model):
    class Meta:
        db_table = "user_number_relations"


    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    uuid = models.UUIDField(editable=False, unique=True, auto_created=True, default=uuid.uuid4)
    number_id = models.ForeignKey(Number, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id} - {self.number_id}'
        