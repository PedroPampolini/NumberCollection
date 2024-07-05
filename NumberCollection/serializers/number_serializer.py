from rest_framework import serializers
from NumberCollection.models.numbers import Number

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ('id', 'uuid', 'number', 'is_prime', 'created_at', 'updated_at')