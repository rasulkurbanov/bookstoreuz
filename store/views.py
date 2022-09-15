import urllib.parse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import redirect
from django.db.models import Count, Case, When, Avg



from .models import Book, UserBookRelation
from .serializers import BookSerializer, UserBookSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class BookListView(ListCreateAPIView):
    queryset = Book.objects.all().annotate(
    annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
    average_rating=Avg('userbookrelation__rate')
    )
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'price', 'author',]
    ordering_fields = ['name', 'price',]
    

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]


#View to get registered via social media (GitHub)
def auth(request):
    return render(request, 'oauth.html')


class UserBookRelationView(mixins.UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserBookRelation.objects.all()
    serializer_class = UserBookSerializer

    

