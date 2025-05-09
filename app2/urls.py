from django.urls import path
from .views import userApiview, user_data

urlpatterns = [
    path('users/',userApiview.as_view(), name='user_list'),
    path('userdata/', user_data, name='userdata')
]
