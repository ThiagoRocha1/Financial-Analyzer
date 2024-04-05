from django.urls import path
from users.views import register,login,logout,account

urlpatterns = [
    path('register/',register, name='register'),
    path('login/', login, name='login'),
    path('logout/',logout,name='logout'),
    path('account/',account,name='account'),
]