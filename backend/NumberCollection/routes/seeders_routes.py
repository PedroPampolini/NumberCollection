from django.urls import re_path
from NumberCollection.views import seeder_view

urlpatterns = [
    re_path(r'^seeduser$', seeder_view.seed_user),
]