from django.contrib import admin
from django.urls import path, include

#urlpatterns = [
#    path('', include('menu.urls')), 
#    path('admin/', admin.site.urls),
#]

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')), 
]
