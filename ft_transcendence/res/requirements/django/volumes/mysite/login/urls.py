from django.urls import path
from . import views

urlpatterns = [
    path('oauth/', views.oauth, name='oauth'),
    path('oauth/callback/', views.oauth_callback, name='oauth_callback'),
]