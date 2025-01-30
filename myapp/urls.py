from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home-page'),
    path('about', views.about, name='about-page'),
    path('contact', views.contact, name='contact-page'),
    path('menu', views.menu, name='menu-page'),
    path('category/<int:cat_id>', views.catProd, name='menu-cat-page'),
    path('details/<int:i_id>', views.prodDetails, name='details-page'),
    path('testimonial', views.testimonial, name='testimonial-page'),
    path('booking', views.booking, name='booking-page'),
    path('user_reg', views.userReg, name='usr-reg-page'),
    path('user_log', views.userLogin, name='usr-log-page'),
    path('user_logout', views.userLogout, name='usr-logout-page'),
    path('add/<int:i_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart', views.view_cart, name='view_cart'),
    path('remove/<int:id>', views.remove_cart, name='remove_cart'),
    path("initiate-payment/", views.initiate_payment, name="initiate_payment"),
    path("payment-success/", views.payment_success, name="payment_success"),
    path("payment-failed/", views.payment_failed, name="payment_failed"),
    path("order_details", views.myOrders, name="order-details-page"),
    path("order_tracking", views.order_track, name="order-tracking-page"),
]