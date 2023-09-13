from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage, name='login'),
    path('register/',views.registerPage, name='register'),
    path('logout/',views.logoutUser, name='logout'),
    path('',views.home,name='home'),
    path('room/<str:pk>/', views.room,name = 'room'),
    path('create-room/',views.createRoom, name='create-room'),
    path('update-room/<str:pk>/',views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/',views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/',views.deleteMessage, name='delete-message'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
    path('user-update', views.updateUser, name='user-update'),
    path('topics/', views.topicsPage , name='topics'),
    path('activities/', views.activitiesPage , name='activities')
]