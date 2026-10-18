from django.urls import path

from user import views

urlpatterns = [
    path('allusers/', views.allUsers),
    path('singleuser/', views.singleUser),
]