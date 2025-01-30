from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path("home/", views.home, name='home'),        # Home page
    path('login/', views.login_page, name='login_page'),    # Login page
    path('register/', views.register_page, name='register'),  # Registration page
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),  # Edit user page
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),  # Delete user page
]