from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('dashBoard',views.dashBoard,name='dashBoard'),
    path('create_session',views.create_session,name='create_session'),
    path('access_session',views.access_session,name='access_session'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
]