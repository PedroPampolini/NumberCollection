from django.urls import include, path
from django.contrib import admin
# Importa as urls dos módulos em /urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('NumberCollection.routes.users_routes')),
    path('', include('NumberCollection.routes.seeders_routes')),
    path('', include('NumberCollection.routes.numbers_routes')),
    path('', include('NumberCollection.routes.users_number_relation_routes')),
]