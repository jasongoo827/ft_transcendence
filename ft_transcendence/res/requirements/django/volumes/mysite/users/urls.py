from django.urls import path

from .views import UsersAPIView, UserAPIView

urlpatterns = [
	path('list/', UsersAPIView.as_view()),
	path('list/<int:id>/', UserAPIView.as_view()),
]
