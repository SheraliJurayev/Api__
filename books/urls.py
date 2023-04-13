from django.urls import path
from .views import BookListApiView , BookDetaiApiView , BookDeleteApiView , BookUpdateApiView , BookCreateApiView

urlpatterns = [
    path('books/' , BookListApiView.as_view()) ,
    path('books/create/' , BookCreateApiView.as_view()) , 
    path('books/<int:pk>/' , BookDetaiApiView.as_view()) ,
    path('books/<int:pk>/delete/' , BookDeleteApiView.as_view()) , 
    path('books/<int:pk>/update/' , BookUpdateApiView.as_view()) , 



]