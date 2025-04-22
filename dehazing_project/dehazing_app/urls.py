from django.urls import path
from .views import register_view, login_view, about_view
from django.contrib.auth.views import LogoutView
from . import views
from dehazing_app import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('upload-image/', views.upload_image, name='upload_image'),  # Placeholder
    path('processing-history/', views.processing_history, name='processing_history'),  # Placeholder
    path('advanced-options/', views.advanced_options, name='advanced_options'),  # Placeholder
    path('dehazing/', views.dehazing_page, name='dehazing_page'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('about/', about_view, name='about'),
    path('api/dehaze/', views.dehaze_api, name='dehaze_api'),
    path('api/dehaze/', views.dehaze_api, name='dehaze_api'),




]

