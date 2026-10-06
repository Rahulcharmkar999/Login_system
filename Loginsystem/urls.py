
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('APP1.urls')),
     path('',include('APP2.urls'))
]
