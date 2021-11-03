from content.api.views import (
    AuthorViewSet,
    BookViewSet,
    CommentCreateViewSet,
    PublisherViewSet,
)
from rest_framework.routers import SimpleRouter

content_router = SimpleRouter()
content_router.register("books", BookViewSet, basename="book")
content_router.register("authors", AuthorViewSet, basename="author")
content_router.register("publishers", PublisherViewSet, basename="publisher")
content_router.register("comments", CommentCreateViewSet, basename="comment")
