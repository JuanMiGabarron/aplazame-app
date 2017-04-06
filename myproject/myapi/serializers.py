from myapp.models import Base
from rest_framework import serializers


# We use serializers from models and select the fields showed by the api
class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ()
