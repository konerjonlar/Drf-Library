from rest_framework import serializers
from content.models import Book, Author,Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'author','age','phone', 'adr',)

class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'isim','image', 'author','description', 'category', 'yayin_evi')


class YorumSerializer(serializers.ModelSerializer):
    yorum_sahibi = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['kitap']