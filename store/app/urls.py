from django.urls import path
from .views import track_order
from .views import cancel_order, booking_confirmation

from .import views

urlpatterns = [
    path('',views.log),
    path('register/',views.reg ,name='register'),
    path('lout',views.lout, name='lout'),
    path('admdash',views.admdash),
    path('add/',views.addp, name='add'),
    path('edit/<str:pid>/', views.editp),
    path('dele/<pid>',views.delp, name='dele'),
    path('upb/',views.update_banner, name='upb'),
    path('addcat/',views.add_cat, name='addcat'),
    path('delecat/<int:cat_id>/',views.dele_cat, name='delecat'),
    path('viewproduct', views.viewp),
    path('u_home',views.uhome, name='u-home'),
    path('addw', views.addws, name='add_weight'),
    path('editweight/<str:pid>/', views.editws, name='edit_weight'),
    path('products/<int:category_id>/', views.product_list, name='product_list'),
    path('search/', views.search_products, name='search_products'),
    path('product/<int:pid>/', views.single_product, name='single_product'),
    path('add-to-cart/<int:pid>/<int:weight_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_page, name='cart_page'),
    path('qout/<int:pk>/', views.qout, name='qout'),
    path('qin/<int:pk>/', views.qin, name='qin'),
    path('cart/remove/<int:pk>/', views.cart_remove, name='cart_remove'),
    path('order-details/', views.order_details, name='orderdetails'),
    path('buy-now/<int:wid>/', views.buy_now, name='buy_now'),
    path('buy/', views.buy, name='buy'),
    path('booking-confirmation', views.booking_confirmation, name='booking_confirmation'),
    path('shop/bookings/', views.admin_bookings, name='admin_bookings'),
    path('About/', views.About, name='about'),
    path('track/<str:tracking_id>/', track_order, name='track_order'),
    
    path('booking-confirmation/', booking_confirmation, name='booking_confirmation'),
    path('cancel_order/<int:order_id>/', cancel_order, name='cancel_order'),
         
]