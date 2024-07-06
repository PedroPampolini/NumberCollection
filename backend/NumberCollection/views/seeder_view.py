from django.views.decorators.csrf import csrf_exempt
from NumberCollection.models.users import User
from NumberCollection.serializers.user_serializer import UserSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from NumberCollection.views import utils
import lorem
import random

@csrf_exempt
def seed_user(request):
    match(request.method):
        case 'POST':
            seeder = JSONParser().parse(request)
            quantity = seeder['quantity'] if 'quantity' in seeder else 1
            for i in range(quantity):
                user_json = generate_user()
                user_serializer = UserSerializer(data=user_json)
                if user_serializer.is_valid():
                    user_serializer.save()
                else:
                    return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse({'message': 'Users seeded'}, status=status.HTTP_201_CREATED)
        case _:
            return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
def generate_user():
    user = UserSerializer().data
    user['username'] = generate_lorem_ipsum(3)
    user['password'] = 'password'
    user['email'] = generate_lorem_ipsum(2).replace(' ','') + '@gmail.com'
    user['phone'] = ''.join([str(random.randint(0, 9)) for i in range(11)])
    user['address'] = generate_lorem_ipsum(10)

    return user



def generate_lorem_ipsum(qtd_words: int):
    # gera um texto com a quantidade de palavras passadas
    return ' '.join(lorem.text().split(' ')[:qtd_words])
