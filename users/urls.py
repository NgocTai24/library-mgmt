from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:user_id>/', views.user_detail, name='user_detail'), 
    path('api/', views.api_user_list, name='api_user_list'), 
]