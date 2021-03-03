from django.contrib import admin
from django.urls import path
from .views import home, signup, login, cart, checkout, order
from .middleware.auth import auth_middleware

urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup', signup.SignUp.as_view(), name="signup"),
    path('login', login.Login.as_view(), name="login"),
    path('logout', login.logout , name="logout"),
    path('cart', cart.Cart.as_view() , name="cart"),
    path('check-out', checkout.CheckOut.as_view(), name="checkout"),
    path('orders', auth_middleware(order.OrderView.as_view()), name="order"),
]
