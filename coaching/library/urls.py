from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="libraryHome"),
    path('singup/', views.singupuser, name="singup"),
    path('login/', views.loginuser, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('book/', views.BookSeats, name="bookSeat"),
    path('cencelseat/<int:seat>', views.cancelSeats, name="bookSeat"),
]

