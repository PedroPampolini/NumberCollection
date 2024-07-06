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

