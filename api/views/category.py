from rest_framework import viewsets, permissions
from rest_framework import filters, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.models import Category
from api.permissions import IsAdmin, IsGetOrIsAdmin
from api.serializers import CategorySerializer


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsGetOrIsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'