from django.urls import path, include
from accounts import views
urlpatterns = [
path ('register',views.register,name='register'),
path('login',views.user_login, name='login'),
path('user-logout',views.user_logout,name='user_logout')
]
