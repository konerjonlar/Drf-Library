from content.api.serializers import (
    AuthorSerializer,
    BookCreateSerializer,
    BookDetailSerializer,
    BookSerializer,
    CommentCreateSerializer,
    PublisherSerializer,
)
from content.models import Author, Book, Comment, Publisher
from rest_framework import filters, generics, mixins, permissions
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class BookViewSet(ModelViewSet):
    queryset = Book.objects.filter(is_active=True)
    serializer_class = BookSerializer
    lookup_field = "slug"
    filter_backends = [filters.SearchFilter]
    search_fields = ("^title",)

    def get_serializer_class(self):
        if self.action == "create":
            return BookCreateSerializer
        if self.action == "retrieve":
            return BookDetailSerializer
        return super().get_serializer_class()


class AuthorViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class PublisherViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet
):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class CommentCreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.filter(is_active=True)
