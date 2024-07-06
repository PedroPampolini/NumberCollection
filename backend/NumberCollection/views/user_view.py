from django.views.decorators.csrf import csrf_exempt
from NumberCollection.models.users import User
from NumberCollection.serializers.user_serializer import UserSerializer
from NumberCollection.views.view_interface import BasicCrud, BasicFilter

class UserView(BasicCrud, BasicFilter):
    def __init__(self):
        super().__init__()  
        self.createCrud(User, UserSerializer)
        self.createFilter(User, UserSerializer)
        self.fields_mapper = {
            'username': 'username',
            'email': 'email',
            'phone': 'phone'
        }

