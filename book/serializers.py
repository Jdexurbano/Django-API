from rest_framework import serializers
from .models import Book

#data searilizers
class BookDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','author','description')