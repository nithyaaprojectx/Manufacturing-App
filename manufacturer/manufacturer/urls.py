from django.contrib import admin
from django.urls import path, include  # Import include
from django.urls import path
from buyer_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('buyer/', include('buyer_app.urls')),
    path('manufacturer/', include('manufacturer_app.urls')),
    path('upload_step_file/', views.upload_step_file, name='upload_step_file'),

]
