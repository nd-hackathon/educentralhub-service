from django.urls import path
from .views import RegisterUserView, LoginView, LogoutView, GetAllUsersView, GetUserByIdView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', GetAllUsersView.as_view(), name='get_all_users'),
    path('users/<int:user_id>/', GetUserByIdView.as_view(), name='get_user_by_id'),
]
