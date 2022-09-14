import urllib.parse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect


from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'price', 'author',]
    ordering_fields = ['name', 'price',]
    

#View to get registered via social media (GitHub)
def auth(request):
    return render(request, 'oauth.html')