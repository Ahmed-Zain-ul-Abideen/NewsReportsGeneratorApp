from django.urls import path
from webApp.views.dashboard import dashboardindexview
from webApp.views.auth import authview

urlpatterns = [
    # Auth Logins
    path('login', authview.UserLoginForm, name="login-dashboard"),
    path('user-login', authview.UserLogin,name="user-login"),
    path('user-logout', authview.UserLogOut,name="user-logout"),


    # Dashboard
    path('', dashboardindexview.index, name='index'),   
]