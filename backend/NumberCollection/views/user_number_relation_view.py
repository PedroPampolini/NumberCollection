from django.views.decorators.csrf import csrf_exempt
from NumberCollection.models.user_number_relations import UserNumberRelations
from NumberCollection.serializers.user_number_relation_serializer import UserNumberRelationsSerializer
from NumberCollection.views.view_interface import BasicCrud

class UserNumberRelationView(BasicCrud):
    def __init__(self):
        super().__init__(UserNumberRelations, UserNumberRelationsSerializer)
        
    

