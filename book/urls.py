from django.urls import path
from . import views

urlpatterns = [
    path('book', views.BookView.as_view()),
    path('book_detail/<int:id>', views.BookView.as_view(), name='book_detail'),

    path('lang_list/', views.BookView.as_view()),
    path('lang_list/<int:id>/delete/', views.BookView.as_view()),
    path('lang_list/<int:id>/update/', views.BookView.as_view()),
    path('create_post_lang/', views.BookView.as_view()),

    path('add-cooment/', views.createBookView),
    path('add-cooment/', views.createBookView),
    path('seacrh/', views.SearchView.as_view(), name='search'),
]
