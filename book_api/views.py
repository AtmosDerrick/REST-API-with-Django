from django.shortcuts import render
from django.http import JsonResponse

from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all() #complex data
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
        
    
    
    
    
