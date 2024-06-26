from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path("accounts/login/", views.login_view),
]
