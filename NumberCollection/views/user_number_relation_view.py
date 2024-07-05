from django.views.decorators.csrf import csrf_exempt
from NumberCollection.models.user_number_relations import UserNumberRelations
from NumberCollection.serializers.user_number_relation_serializer import UserNumberRelationsSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from NumberCollection.views import utils

@csrf_exempt
def usernumberrelationcrud(request, id=-1):
    match(request.method):
        case 'GET':
            if id == -1:
                usr = UserNumberRelations.objects.all()
                user_num_relation_serializer = UserNumberRelationsSerializer(usr, many=True)
                return JsonResponse(user_num_relation_serializer.data, safe=False)
            elif UserNumberRelations.objects.filter(id=id).exists():
                usr = UserNumberRelations.objects.get(id=id)
                user_num_relation_serializer = UserNumberRelationsSerializer(usr)
                return JsonResponse(user_num_relation_serializer.data, safe=False, status=status.HTTP_200_OK)
            else:
                return utils.make_not_found_response('User', id)

        case 'POST':
            usr = JSONParser().parse(request)
            user_num_relation_serializer = UserNumberRelationsSerializer(data=usr)
            if user_num_relation_serializer.is_valid():
                user_num_relation_serializer.save()
                return JsonResponse(user_num_relation_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(user_num_relation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        case 'PUT':
            usr = JSONParser().parse(request)
            # if not User.objects.filter(id=id).exists():
            #     return utils.make_not_found_response('User', id)
            usr = UserNumberRelations.objects.get(id=usr['id'])
            user_num_relation_serializer = UserNumberRelationsSerializer(usr, data=usr)
            if user_num_relation_serializer.is_valid():
                user_num_relation_serializer.save()
                return JsonResponse(user_num_relation_serializer.data, status=status.HTTP_200_OK)
            return utils.update_not_valid_response()       

        case 'DELETE':
            if UserNumberRelations.objects.filter(id=id).exists():
                usr = UserNumberRelations.objects.get(id=id)
                usr.delete()
                return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return utils.make_not_found_response('User', id)