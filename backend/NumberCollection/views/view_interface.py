from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpRequest
from NumberCollection.views import utils
from rest_framework.serializers import ModelSerializer
from NumberCollection.models.model import BasicModel
from django.db.models import Q
from typing import *

class BasicCrud():
    def createCrud(self, model:BasicModel, serializer:ModelSerializer):
        self.Model:BasicModel = model
        self.Serializer:ModelSerializer = serializer

    def GET(self, request:HttpRequest, uuid=''):
        if uuid == '':
            data = self.Model.objects.all()
            serializer:ModelSerializer= self.Serializer(data, many=True)
            return JsonResponse(serializer.data, safe=False)
        elif self.Model.objects.filter(uuid=uuid).exists():
            data = self.Model.objects.get(uuid=uuid)
            serializer:ModelSerializer = self.Serializer(data)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            return utils.make_not_found_response(self.Model.__name__, uuid)

    def POST(self, request:HttpRequest):
        data = JSONParser().parse(request)
        serializer:ModelSerializer = self.Serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def PUT(self, request:HttpRequest):
        data = JSONParser().parse(request)
        uuid = data['uuid'] if 'uuid' in data else ''
        if not self.Model.objects.filter(uuid=uuid).exists():
            return utils.make_not_found_response(self.Model.__name__, uuid)
        data = self.Model.objects.get(uuid=uuid)
        serializer:ModelSerializer = self.Serializer(data, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return utils.update_not_valid_response()    

    def DELETE(self, request:HttpRequest, uuid=''):
        if self.Model.objects.filter(uuid=uuid).exists():
            data = self.Model.objects.get(uuid=uuid)
            data.delete()
            return JsonResponse({'message': f'{self.Model.__name__} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        return utils.make_not_found_response(self.Model.__name__, id)

    @csrf_exempt
    def crud(self, request:HttpRequest,uuid=''):
        match(request.method):
            case 'GET':
                return self.GET(request, uuid)
            case 'POST':
                return self.POST(request)
            case 'PUT':
                return self.PUT(request)
            case 'DELETE':
                return self.DELETE(request, uuid)
            
class BasicFilter():
    def createFilter(self, model:BasicModel, serializer:ModelSerializer, supported_operators:List[str] = None):
        self.Model:BasicModel = model
        self.Serializer:ModelSerializer = serializer
        self.fields_mapper:Dict[str,str] = {}
        self.operator_map:Dict[str,str] = {
            '>': 'gt',
            '>=': 'gte',
            '<': 'lt',
            '<=': 'lte',
            "!=": 'ne',
            'not_sensitive_has': 'contains',
            'not_has': 'icontains',
            'sensitive_has': 'contains',
            'has': 'icontains',
            'is': 'exact',
            'not_is': 'exact',
        }
    
    def MapFields(self, filter:Dict[str,str]):
        return {self.fields_mapper[key]: value for key,value in filter.items() if key in self.fields_mapper}

    
    def filter_mapper(self, operator:str, key:str, value:str):
        if operator.startswith('not_'):
            for op in self.operator_map:
                if operator == op:
                    return ~Q(**{f'{key}__{self.operator_map[op]}': value})
        else:
            for op in self.operator_map:
                if operator == op:
                    return Q(**{f'{key}__{self.operator_map[op]}': value})
            

    @csrf_exempt
    def search(self, request:HttpRequest):
        filterForm = self.MapFields(JSONParser().parse(request))
        print(filterForm)
        # filtra os dados que não existem no modelo
        model_fields = [field.name for field in self.Model._meta.get_fields()]
        filterForm = {key: value for key,value in filterForm.items() if key in model_fields}
        
        filter_expressions = Q()
        try:
            for key, value in filterForm.items():
                if key in model_fields:
                    if isinstance(value, str):
                        if ' ' in value:
                            operator, *field = value.split(' ')
                            field = ' '.join(field)
                            if operator in self.operator_map:
                                filter_expressions &= self.filter_mapper(operator, key, field)
                        else:
                            filter_expressions &= Q(**{key: value})
                    else:
                        filter_expressions &= Q(**{key: value})
        except Exception as e:
            print(e)
            return JsonResponse({'message': 'Invalid filter'}, status=status.HTTP_400_BAD_REQUEST)

        data = self.Model.objects.filter(filter_expressions)
        serializer:ModelSerializer = self.Serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
