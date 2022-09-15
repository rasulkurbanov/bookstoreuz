from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Book, UserBookRelation


class BookSerializer(ModelSerializer):
    annotated_likes = serializers.IntegerField(read_only=True)
    average_rating = serializers.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        model = Book
        fields = ['id', 'name', 'price', 'author', 'annotated_likes', 'owner', 'average_rating']

        
class UserBookSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ['book', 'like', 'in_bookmarks', 'rate']