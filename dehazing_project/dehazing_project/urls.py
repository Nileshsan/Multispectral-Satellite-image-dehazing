"""
URL configuration for dehazing_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from dehazing_app import views
from django.conf.urls.static import static
from django.conf import settings



def main_page(request):
    return render(request, 'index.html')  # Render the main page

def dehazing_page(request):
    return render(request, 'dehazing_page.html')  # Render the dehazing page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),  # Main page
    path('dehazing/', dehazing_page, name='dehazing_page'),  # Add this for 'dehazing_page'
    path('users/', include('dehazing_app.urls', namespace='users')),
    path('api/dehaze/', views.dehaze_api, name='dehaze_api'),
    path('about/', views.about_view, name='about'),  # Add this for 'about' page

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)