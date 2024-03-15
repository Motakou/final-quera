from django.urls import path
from .views import createc,readc,listc,deletec,usersingup,userlogin,userlogout


urlpatterns = [
    path('new/', createc,name="create"),
    path('read/<int:id>/',readc,name="read"),
    path('list/',listc,name="all-c"),
    path('delete/<int:id>/',deletec,name='delete'),
    path('signup/',usersingup,name="register"),
    path('login/',userlogin,name='login'),
    path('logout/',userlogin,name='logout'),
]
