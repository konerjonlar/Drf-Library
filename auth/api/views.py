from auth.api.serializers import UserCreateSerializer
from auth.models import User
from rest_framework import filters, generics, mixins, permissions
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class UserCreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserCreateSerializer
    queryset = User.objects.filter(is_active=True)
    permission_classes = (permissions.AllowAny,)
