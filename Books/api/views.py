from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .serializers import BooksSerializer
from ..models import Books


class BooksListAPIView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksDetailAPIView(RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = "pk"


class BooksDeleteAPIView(DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = "pk"


class BooksUpdateAPIView(UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = "pk"