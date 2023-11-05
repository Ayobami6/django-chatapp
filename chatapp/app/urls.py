from django.urls import path
from .views import HomeView, UserCreateView, LoginInterface, LogoutInterface

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("signup/", UserCreateView.as_view(), name="signup"),
    path('logout/', LogoutInterface.as_view(), name='logout'),
    path('login/', LoginInterface.as_view(), name='login'),

]
