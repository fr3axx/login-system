from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', views.home, name='home'),        # Home page
    path('signin/', views.login_page, name='signin'),    # Login page
    path('signout/', views.signout, name='signout'),  # Logout page
    path('signup/', views.signup, name='signup'),  # Registration page
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),  # Edit user page
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),  # Delete user page

    #ADMIN
    path('admincito/', views.admin_page, name='admin_page'),  # Admin page
    path('access_denied/', views.access_denied, name='access_denied'),  # Access denied page
    
]