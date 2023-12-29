from rest_framework import serializers
from .models import Car, Book, Film, Notebook

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['model', 'price']

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class FilmSerializers(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'

class NotebookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Notebook
        fields = '__all__'