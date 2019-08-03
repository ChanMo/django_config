from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *


class ConfigViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
    获取系统配置
    """
    model = Config
    permission_classes = (AllowAny,)
    serializer_class = ConfigSerializer
    pagination_class = None
    queryset = Config.objects.all()
    lookup_field = 'code'
