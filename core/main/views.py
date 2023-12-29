from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarSerializers,BookSerializers, FilmSerializers, NotebookSerializers
from .models import Car, Book, Film, Notebook
# Create your views here.


class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

class BookView(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializers

class FilmView(viewsets.ModelViewSet):

    queryset = Film.objects.all()
    serializer_class = FilmSerializers

class NotebookView(viewsets.ModelViewSet):

    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializers