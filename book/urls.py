from django.urls import path
from . import views

urlpatterns = [
    path('book', views.book_view),
    path('book_detail/<int:id>', views.book_detail_view, name='book_detail'),
    path('', views.home, name='home'),

    path('lang_list/', views.book_delete_view),
    path('lang_list/<int:id>/delete/', views.book_drop_view),
    path('create_post_lang/', views.createLangPostView),

    path('add-cooment/', views.createBookView),
    path('add-cooment/', views.createBookView),
]
