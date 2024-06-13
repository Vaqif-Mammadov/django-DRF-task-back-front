from django.urls import path
from .views import (
    BooksListAPIView,
    BooksDetailAPIView,
    BooksUpdateAPIView,
    BooksDeleteAPIView,
)

urlpatterns = [
    path("list/", BooksListAPIView.as_view(), name="api-list"),
    path("detail/<pk>", BooksDetailAPIView.as_view(), name="api-detail"),
    path("update/<pk>", BooksUpdateAPIView.as_view(), name="api-update"),
    path("delete/<pk>", BooksDeleteAPIView.as_view(), name="api-delete"),
]