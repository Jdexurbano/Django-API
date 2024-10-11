from django.http import Http404
from rest_framework.response import Response
from .serializers import BookDataSerializers
from .models import Book
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


#class based views
class BookListView(APIView):
    
    #get all all the book in the model
    def get(self,request,format = None):
        book = Book.objects.all()
        serializer = BookDataSerializers(book, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #add a new book
    def post(self,request,format = None):
        #serialize the new input data
        serializer = BookDataSerializers(data = request.data)
        
        #check if the data is valid
        if serializer.is_valid():
            #if the data is valid
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #if the data is not valid
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    
    #check if the Book is exist in the database
    def get_object(self,pk):
        try:
            return Book.objects.get(pk = pk)
        except Book.DoesNotExist:
            raise Http404

    #get the correspond book
    def get(self,request,pk,format = None):
        #get the pk of the book
        book = self.get_object(pk)
        serializer = BookDataSerializers(book)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #edit task
    def put(self,request,pk,format = None):
        book = self.get_object(pk)
        serializer = BookDataSerializers(book,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #delete task
    def delete(self,request,pk,format = None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)