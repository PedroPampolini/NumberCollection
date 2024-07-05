from django.views.decorators.csrf import csrf_exempt
from NumberCollection.models.users import User
from NumberCollection.serializers.user_serializer import UserSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from NumberCollection.views import utils

@csrf_exempt
def usercrud(request, id=-1):
    match(request.method):
        case 'GET':
            if id == -1:
                users = User.objects.all()
                user_serializer = UserSerializer(users, many=True)
                return JsonResponse(user_serializer.data, safe=False)
            elif User.objects.filter(id=id).exists():
                user = User.objects.get(id=id)
                user_serializer = UserSerializer(user)
                return JsonResponse(user_serializer.data, safe=False, status=status.HTTP_200_OK)
            else:
                return utils.make_not_found_response('User', id)

        case 'POST':
            user = JSONParser().parse(request)
            user_serializer = UserSerializer(data=user)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        case 'PUT':
            user = JSONParser().parse(request)
            # if not User.objects.filter(id=id).exists():
            #     return utils.make_not_found_response('User', id)
            user = User.objects.get(id=user['id'])
            user_serializer = UserSerializer(user, data=user)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)
            return utils.update_not_valid_response()       

        case 'DELETE':
            if User.objects.filter(id=id).exists():
                user = User.objects.get(id=id)
                user.delete()
                return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return utils.make_not_found_response('User', id)