from django.urls import path

from . import views

urlpatterns = [
    path('cart',views.cart,name='cart'),
    path('add/<int:product_id>',views.add_cart,name='addcart'),
    path('dec/<int:product_id>', views.min_cart, name='dec_cart'),
    path('del/<int:product_id>', views.cart_delete, name='del_cart'),

]