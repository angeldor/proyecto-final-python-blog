from django.urls import path
from .views import SingUp, Login

urlpatterns = [
    path('singup/', SingUp.as_view(), name='singup'),
    path('login', Login.as_view(), name='login')
        
]
