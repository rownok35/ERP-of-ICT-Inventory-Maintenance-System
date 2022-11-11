from django.urls import path
from . import views

app_name = 'profiles'



urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('create-user/', views.sign_up, name='create-user'),
    path('profile/', views.profile, name='profile'),
    path('change-profile/', views.user_profile, name='user-profile'),
    path('password/', views.pass_change, name='pass_change'),

]
