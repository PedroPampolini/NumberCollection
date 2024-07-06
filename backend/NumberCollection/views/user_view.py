from django.views.decorators.csrf import csrf_exempt
from NumberCollection.models.users import User
from NumberCollection.serializers.user_serializer import UserSerializer
from NumberCollection.views.view_interface import BasicCrud

class UserView(BasicCrud):
    def __init__(self):
        super().__init__(User, UserSerializer)        
