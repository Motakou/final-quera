from django.urls import path
from .views import createc, readc, listc, deletec, signup, login, logout


urlpatterns= [
    path('new-critic/', createc, name='create'),
    path('read/<int:id>', readc, name='read'),
    path('criticslist/', listc, name='list'),
    path('deletecritic/<int:id>', deletec, name='delete'),
    path('signup/', signup, name= 'register'),
    path('userlogin/', login, name='login'),
    path('userlogout/', logout, name='logout')
]