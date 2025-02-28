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
    path('admincito/edit_user/<int:user_id>/', views.edit_user_admin, name='edit_user_admin'),  # Edit user page
    path('access_denied/', views.access_denied, name='access_denied'),  # Access denied page
    
    #PRODUCTOS
    path('productos/', views.productos, name='productos'),  # Productos page
    path('producto_detalles/<int:producto_id>', views.producto_detalles, name='producto_detalles'),
    

    #CARRITO
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),  # Ver carrito page
    path('ver_carrito/agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'), # Add to cart page
    path('ver_carrito/eliminar_del_carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),  # Remove from cart page
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('facturacion/', views.facturacion, name='facturacion'),  # Billing page
    path('generar_factura_pdf/', views.generar_factura_pdf, name='generar_factura_pdf'),
]