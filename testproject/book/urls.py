from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.BookListView.as_view(), name='index'),
    # path('detail/<slug:slug>/', views.detail, name='detail'),
    path('detail/<slug:slug>/', views.BookDetailView.as_view(), name='detail'),
    path('book_add/', views.book_add, name='book_add'),
    path('cart/add/<slug:slug>', views.cart_add, name='cart_add'),
    path('cart/list/', views.cart_list, name='cart_list'),
    path('cart/delete/<slug:slug>', views.cart_delete, name='cart_delete'),
]