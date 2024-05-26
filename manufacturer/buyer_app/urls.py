from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in login views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='buyer/login.html'), name='login'),
    path('upload/', views.upload_file, name='upload_file'),
    path('success/', views.success, name='success'),
    path('upload_step_file/', views.upload_step_file, name='upload_step_file'),
]

