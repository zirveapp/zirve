from django.urls import path
from app.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='app'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
]