"""
URL configuration for core project.

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
# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from authentication.views import edit_user, delete_user
from authentication.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.conf.urls.static import static  # Static files serving
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving

# Define URL patterns
urlpatterns = [
    path('<int:user_id>', home, name="home_page"),      # Home page
    path("admin/", admin.site.urls),          # Admin interface
    path('login/', login_page, name='login_page'),    # Login page
    path('register/', register_page, name='register'),  # Registration page
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),  # Edit user page
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),  # Delete user page
]

# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()