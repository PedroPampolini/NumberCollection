from django.urls import re_path
from NumberCollection.views.user_number_relation_view import UserNumberRelationView

user_number_relation_view = UserNumberRelationView()

urlpatterns = [
    re_path(r'^api/usernumberrelation$', user_number_relation_view.crud),
    re_path(r'^api/usernumberrelation/([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$', user_number_relation_view.crud),
]

