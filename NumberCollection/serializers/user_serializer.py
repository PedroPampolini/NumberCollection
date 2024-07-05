from rest_framework import serializers
from NumberCollection.models.users import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uuid', 'username', 'password', 'email', 'phone', 'address', 'created_at', 'updated_at')