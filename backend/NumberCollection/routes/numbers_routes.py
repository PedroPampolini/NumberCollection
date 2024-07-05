from django.urls import re_path
from NumberCollection.views import number_view

urlpatterns = [
    re_path(r'^api/numbers$', number_view.numbercrud),
    re_path(r'^api/numbers/([0-9]+)$', number_view.numbercrud),
]

