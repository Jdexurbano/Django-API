from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookDataSerializers
from .models import Book
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serialize_data = BookDataSerializers(books,many = True)
        data = serialize_data.data
        return Response(data,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = BookDataSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
        return Response(data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def book_detail(request,id):
    
    is_exist = Book.objects.filter(id = id).exists()
    
    if is_exist:
        book = Book.objects.get(id = id)

        if request.method == 'GET':
            serializer = BookDataSerializers(book)
            data = serializer.data
            return Response(data,status.HTTP_200_OK)
        
        if request.method == 'PUT':
            serializer = BookDataSerializers(book,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
               
            return Response(serializer.errors,status=status.HTTP_201_CREATED)
        
        if request.method == 'DELETE':
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_404_NOT_FOUND)