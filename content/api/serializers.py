from auth.api.serializers import UserCommentSerializer
from auth.models import User
from content.models import Author, Book, Comment, Publisher
from django.utils.text import slugify
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "age", "phone", "address")


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ("id", "name", "city", "year")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "book",
            "text",
        )

    def create(self, validated_data):
        validated_data["from_user"] = self.context["request"].user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    from_user = UserCommentSerializer()

    class Meta:
        model = Comment
        fields = ("id", "from_user", "text")


class BookBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "title",
            "image",
            "author",
            "description",
            "category",
            "publisher",
            "score",
            "created_at",
            "update_at",
        )


class BookSerializer(BookBaseSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "owner",
            "slug",
        ) + BookBaseSerializer.Meta.fields
        extra_kwargs = {"slug": {"read_only": True}}


class BookDetailSerializer(BookBaseSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            "id",
            "owner",
            "slug",
            "comments",
        ) + BookBaseSerializer.Meta.fields

    def get_comments(self, obj):
        return CommentSerializer(Comment.objects.filter(book_id=obj.id), many=True).data


class BookCreateSerializer(BookBaseSerializer):
    class Meta:
        model = Book
        fields = BookBaseSerializer.Meta.fields

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        validated_data["slug"] = slugify(validated_data["title"])
        return super().create(validated_data)
