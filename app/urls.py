from django.urls import path
from .views import UserList, UserDetails

urlpatterns = [
    path('users_list', UserList.as_view(), name='users_list'),
    path('user_detail/<int:pk>', UserDetails.as_view(), name='user_detail'),
]