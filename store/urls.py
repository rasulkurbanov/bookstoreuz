from django.urls import path, include

from .views import BookView

urlpatterns = [
    path('books', BookView.as_view()),
]