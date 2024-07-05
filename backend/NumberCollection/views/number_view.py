from django.views.decorators.csrf import csrf_exempt
from NumberCollection.models.numbers import Number
from NumberCollection.serializers.number_serializer import NumberSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from NumberCollection.views import utils

@csrf_exempt
def numbercrud(request, id=-1):
    match(request.method):
        case 'GET':
            if id == -1:
                numbers = Number.objects.all()
                number_serializer = NumberSerializer(numbers, many=True)
                return JsonResponse(number_serializer.data, safe=False)
            elif Number.objects.filter(id=id).exists():
                number = Number.objects.get(id=id)
                number_serializer = NumberSerializer(number)
                return JsonResponse(number_serializer.data, safe=False, status=status.HTTP_200_OK)
            else:
                return utils.make_not_found_response('Number', id)

        case 'POST':
            number = JSONParser().parse(request)
            number_serializer = NumberSerializer(data=number)
            
            if number_serializer.is_valid():
                number_serializer.validated_data['is_prime'] = is_prime(number['number'])
                number_serializer.save()
                return JsonResponse(number_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(number_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        case 'PUT':
            number = JSONParser().parse(request)
            # if not Number.objects.filter(id=id).exists():
            #     return utils.make_not_found_response('User', id)
            number = Number.objects.get(id=number['id'])
            number_serializer = NumberSerializer(number, data=number)
            if number_serializer.is_valid():
                number_serializer.save()
                return JsonResponse(number_serializer.data, status=status.HTTP_200_OK)
            return utils.update_not_valid_response()       

        case 'DELETE':
            if Number.objects.filter(id=id).exists():
                number = Number.objects.get(id=id)
                number.delete()
                return JsonResponse({'message': 'Number was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return utils.make_not_found_response('Number', id)
        

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    return True