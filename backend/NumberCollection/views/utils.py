from rest_framework import status
from django.http.response import JsonResponse

NO_DATA_FOUND = {'error':'404','message': 'No data found'}

def make_not_found_response(object_name: str, object_id: int):
    return JsonResponse({'message': f'{object_name} with id {object_id} not found'}, status=status.HTTP_404_NOT_FOUND)

def update_not_valid_response():
    return JsonResponse({'message': 'Update not valid'}, status=status.HTTP_400_BAD_REQUEST)