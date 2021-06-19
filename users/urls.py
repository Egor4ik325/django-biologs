from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Default Django authentication urls (like login, logout, etc.)
    path('', include('django.contrib.auth.urls')),

    # My urls (custom logging functionality) (+ url short naming)
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
]
