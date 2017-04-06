from myapp.models import Curso
from rest_framework import serializers


# We use serializers from models and select the fields showed by the api
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'nombre', 'descripcion', 'fecha_inicio',
            'fecha_fin', 'cocinero', 'alumnos')
