from django.conf.urls import url, include
from rest_framework import routers
from myapi.viewsets import CursoViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('cursos', CursoViewSet, 'cursos')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
