from myapp.models import Curso
from myapi.serializers import CursoSerializer
from rest_framework.viewsets import ModelViewSet


# viewset of the api, the display all the object ordered by date_booked
class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all().order_by('nombre')
    serializer_class = CursoSerializer
