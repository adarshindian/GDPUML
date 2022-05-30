from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('dashBoard',views.dashBoard,name='dashBoard'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
]