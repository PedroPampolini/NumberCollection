from django.urls import re_path
from NumberCollection.views import seeder_view

urlpatterns = [
    re_path(r'^seedusers$', seeder_view.seed_user),
]