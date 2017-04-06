from myapp.models import Base
from myapi.serializers import TradeSerializer
from rest_framework.viewsets import ModelViewSet


# viewset of the api, the display all the object ordered by date_booked
class BaseViewSet(ModelViewSet):
    queryset = Base.objects.all().order_by('-date_booked')
    serializer_class = TradeSerializer
