from django import urls
from django.urls import path

from .views import  DeleteUserView, HomePageView,AddUserView ,DetailPageView, UpdateUserView

app_name = 'myapp'

urlpatterns = [
     path('',HomePageView.as_view(),name="index"),
     path('detail/<str:pk>',DetailPageView.as_view(),name="detail"),
     path('add/',AddUserView.as_view(),name="add"),
     # path('delete-img/<str:pk>', deleteImage,name="delete-img"),
     path('delete/<int:id>', DeleteUserView.as_view(),name='delete'),
     path('update/<str:pk>', UpdateUserView.as_view(),name='update'),
  
]