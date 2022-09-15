from django.urls import path, include
from rest_framework import routers

from .views import BookDetailView, BookListView, UserBookRelationView

router = routers.DefaultRouter()
router.register(r'bookrelation', UserBookRelationView)

urlpatterns = [
    path('books', BookListView.as_view()),
    path('books/<int:pk>', BookDetailView.as_view()),
    path('', include(router.urls))
]
