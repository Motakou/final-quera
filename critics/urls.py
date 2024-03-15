from django.urls import path
from .views import createc, readc, listc, deletec, usersignup, userlogin, userlogout


urlpatterns= [
    path('new/', createc, name='create'),
    path('read/<int:id>', readc, name='read'),
    path('list/', listc, name='list'),
    path('delete/<int:id>', deletec, name='delete'),
    path('signup/', usersignup, name= 'register'),
    path('login/', userlogin, name='login'),
    path('logout/', userlogout, name='logout')
]