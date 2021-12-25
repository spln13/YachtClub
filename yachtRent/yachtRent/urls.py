"""yachtRent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Apps import firstPage
from Apps import login
from Apps import signup
from Apps import home
from Apps import lease
from Apps import yacht


urlpatterns = [
    path('', firstPage.show_first_page),
    path('admin/', admin.site.urls),
    path('login/',  login.login),
    path('home/', home.home),
    path('signup/', signup.register),
    path('api/login/verify/', login.login_verify),
    path('api/register/check_username', signup.check_username),
    path('api/register/storage', signup.storage),
    path('api/lease', lease.lease),
    path('api/yacht/query', yacht.getAllYacht),
]
