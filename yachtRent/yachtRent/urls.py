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
from django.urls import path
from Apps import firstPage
from Apps import login
from Apps import signup
from Apps import home
from Apps import lease
from Apps import yacht
from Apps import user


urlpatterns = [
    path('', firstPage.show_first_page),
    path('admin/',  login.admin),
    path('login/',  login.login),
    path('adminLogin/',  login.adminLogin),
    path('home/', home.home),
    path('signup/', signup.register),
    path('lease/', lease.lease_html),
    path('myrecords/', lease.myrecord),
    path('addUser/', user.addUserHTML),
    path('adminYacht/', yacht.adminYachtHTML),
    path('addYacht/', yacht.publish),
    path('adminRecords/', yacht.adminRecords),
    path('api/login/verify/', login.loginVerify),
    path('api/register/check_username', signup.check_username),
    path('api/register/storage', signup.storage),
    path('api/lease/lease', lease.lease),
    path('api/lease/returnyacht', lease.returnYacht),
    path('api/yacht/publish', yacht.publish),
    path('api/yacht/query', yacht.getAllYacht),
    path('api/yacht/getmyrentrecords', yacht.getMyRentRecords),
    path('api/yacht/getAllRecords', yacht.getAllRecords),
    path('api/yacht/delete', yacht.delete),
    path('api/user/adduser', user.addUser),
    path('api/user/deleteuser', user.deleteUser),
    path('api/user/getalluser', user.getAllUser),
    path('api/user/updateuserinfo', user.updateUser),
    path('api/login/adminverify', login.adminVerify),
    path('api/login/userlogout', login.userLogout),
    path('api/login/adminlogout', login.adminLogout),
    path('api/user/getusername', user.getUsername),
    path('api/user/getadminname', user.getAdminname),
]
