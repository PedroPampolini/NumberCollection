from rest_framework import serializers
from NumberCollection.models.user_number_relations import UserNumberRelations

class UserNumberRelationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNumberRelations
        fields = ('id', 'uuid', 'number_id', 'user_id', 'created_at', 'updated_at')

