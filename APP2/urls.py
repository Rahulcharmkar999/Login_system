# APP2 urls

from django.urls import path
from Login_system.APP2.views import *

urlpatterns = [

    path('signup/',signup, name='signup'),
    path('login/',emplogin, name='login'),
    path('empdash/', gotoEmpDashboard, name='gotoEmpdashboard'),
    path('/logout',llogout,name='logout')
]