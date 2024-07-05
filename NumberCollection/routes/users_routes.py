from django.urls import re_path
from NumberCollection.views import user_view

urlpatterns = [
    re_path(r'^api/users$', user_view.usercrud),
    re_path(r'^api/users/([0-9]+)$', user_view.usercrud),
]

