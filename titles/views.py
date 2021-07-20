from django.db.models.aggregates import Avg
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response

from .models import Genre, Category, Title
from .serializers import (GenreSerializer,
                          CategorySerializer,
                          TitleSerializer,
                          TitlePostSerializer)
from users.permissions import IsAdminOrReadOnly
from .filters import TitleFilter


class QueryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# твоим способом тоже получилось, но так как будто проще, чем с миксинами


class CategoryViewSet(QueryViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class GenreViewSet(QueryViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PageNumberPagination
    filterset_class = TitleFilter

    def get_serializer_class(self):
        actions = ['list', 'retrieve']
        if self.action in actions:
            return TitleSerializer
        return TitlePostSerializer
