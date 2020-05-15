from django.urls import path, include
from . import views
# from ..stock_control import views
from stock_control.views import stock_list 

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.stock_list, name="home"),
]

