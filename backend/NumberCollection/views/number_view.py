from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from NumberCollection.models.numbers import Number
from NumberCollection.serializers.number_serializer import NumberSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from NumberCollection.views import utils
from NumberCollection.views.view_interface import BasicCrud, BasicFilter


class NumberView(BasicCrud, BasicFilter):
    def __init__(self):
        super().__init__()
        self.createCrud(Number, NumberSerializer)
        self.createFilter(Number, NumberSerializer)
        self.fields_mapper = {
            'number': 'number',
            'prime': 'is_prime'
        }

    def POST(self, request: HttpRequest):
        number = JSONParser().parse(request)
        number_serializer = NumberSerializer(data=number)
        
        if number_serializer.is_valid():
            number_serializer.validated_data['is_prime'] = self.is_prime(number['number'])
            number_serializer.save()
            return JsonResponse(number_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(number_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def is_prime(self,number):
        if number < 2:
            return False
        for i in range(2, number//2 + 1):
            if number % i == 0:
                return False
        return True
