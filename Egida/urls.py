from django.contrib import admin
from django.urls import path, include

from main.admin_actions import *

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt'))
]

custom_admin_urls = (
    path('admin/main/schools/export/', export, name="export"),
    path('admin/main/schools/update/', update, name="update"),
    path('admin/main/schools/imp/', imp, name="import")
)

urlpatterns += custom_admin_urls
