from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .models import Book, Genre
class BookApiView(APIView):

    def get(self, request: Request):
        books = Book.objects.all()
        book_list = []

        for book in books:
            book_list.append(
                {
                    "name": book.name,
                    "introduction": book.introduction,
                    "price": book.price,
                }
            )
        return Response(book_list)

    def post(self, request: Request):
        book = Book.objects.create(**request.data)
        book_dict = model_to_dict(book)
        del  book_dict['image']
        return Response(book_dict, status=201)


class BookDetailAPIView(APIView):
    def get(self, request: Request, pk):
        book = get_object_or_404(Book, pk=pk)
        book_dict = model_to_dict(book)
        del book_dict['image']
        return Response(book_dict)

class  BookUpdateApiView(APIView):
    def put(self, request: Request, pk):
        book = get_object_or_404(Book, pk=pk)
        for key, value in request.data.items():
            setattr(book, key, value)
        book.save()
        book_dict = model_to_dict(book)
        del   book_dict['image']
        return Response(book_dict)

class BookDeleteApiView(APIView):
    def delete(self, request: Request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=201)

