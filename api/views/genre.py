from rest_framework import filters

from api.mixins import CreateListDestroyMixin
from api.models import Genre
from api.permissions import IsGetOrIsAdmin
from api.serializers import GenreSerializer


class GenreViewSet(CreateListDestroyMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsGetOrIsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
