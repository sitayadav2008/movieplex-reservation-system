from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_view, name='home'),
     path('book/<int:movie_id>/', views.book_ticket, name='book_ticket'),
    path('movies/', views.movie_view, name='movie_page'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('book/<int:movie_id>/', views.book_movie, name='book_movie'),  # Booking page for each movie
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book/<int:movie_id>/', views.book_ticket, name='book_ticket'),
    path('payment/', views.payment, name='payment'),
    
]
