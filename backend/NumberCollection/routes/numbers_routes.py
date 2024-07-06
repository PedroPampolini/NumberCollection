from django.urls import re_path
from NumberCollection.views.number_view import NumberView

number_view = NumberView()

urlpatterns = [
    re_path(r'^api/numbers$', number_view.crud),
    re_path(r'^api/numbers/([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$', number_view.crud),
    re_path(r'^api/numbers/search$', number_view.Search)
]

