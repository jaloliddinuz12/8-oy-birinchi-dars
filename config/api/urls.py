from django.urls import path
from .views import (
    BookApiView,
    BookDetailAPIView,
    BookUpdateApiView,
    BookDeleteApiView,
)

urlpatterns = [

    path('books/', BookApiView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view(), name='book-delete'),
]