from django.urls import re_path
from NumberCollection.views.user_view import UserView

userView = UserView()

urlpatterns = [
    re_path(r'^api/users$', userView.crud),
    re_path(r'^api/users/([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$', userView.crud),
]

