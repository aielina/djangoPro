from django.urls import path
from . import views

urlpatterns = [
    path('book', views.book_view),
    path('book_detail/<int:id>', views.book_detail_view, name='book_detail'),
    path('', views.home, name='home'),
    path('add-cooment/', views.createBookView),
]
