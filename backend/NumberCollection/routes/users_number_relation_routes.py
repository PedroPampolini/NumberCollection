from django.urls import re_path
from NumberCollection.views import user_number_relation_view

urlpatterns = [
    re_path(r'^api/usernumberrelation$', user_number_relation_view.usernumberrelationcrud),
    re_path(r'^api/usernumberrelation/([0-9]+)$', user_number_relation_view.usernumberrelationcrud),
]

