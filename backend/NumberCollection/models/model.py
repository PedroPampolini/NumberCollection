import uuid
from django.db import models

# marca para que o Django saiba que esta classe não é um model
class BasicModel(models.Model):
    class Meta:
        abstract = True
        
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(editable=False, unique=True, auto_created=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
