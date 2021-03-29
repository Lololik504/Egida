from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from Egida import settings
from main.admin_actions import *

schema_view = get_schema_view(
    openapi.Info(
        title="Egida API docs",
        default_version='v1',
        description="Egida API docs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

extra_urlpatterns = [
                        path('', include('main.urls')),
                        path('main/', include('main.urls')),
                        path('accounts/', include('accounts.urls')),
                        path('auth/', include('djoser.urls')),
                        path('auth/', include('djoser.urls.authtoken')),
                        path('auth/', include('djoser.urls.jwt')),
                        url(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=0),
                            name='schema-json'),
                        url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                        url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                    + static(settings.DOCUMENT_URL, document_root=settings.DOCUMENT_ROOT) \
                    + static(settings.ORDERS_URL, document_root=settings.ORDERS_ROOT) \
                    + static(settings.ROSPOTREB_URL, document_root=settings.ROSPOTREB_ROOT)\
                    + static(settings.GOSPOZH_URL, document_root=settings.GOSPOZH_ROOT)\
                    + static(settings.ROSTECH_URL, document_root=settings.ROSTECH_ROOT)\
                    + static(settings.SUDEB_URL, document_root=settings.SUDEB_ROOT)\
                    + static(settings.OTHER_ORDERS_URL, document_root=settings.OTHER_ORDERS_ROOT) \
                    + static(settings.BUILDING_MEDIA_URL, document_root=settings.BUILDING_MEDIA_ROOT) \
                    + static(settings.ENGINEERING_COMMUNICATION_URL, document_root=settings.ENGINEERING_COMMUNICATION_ROOT)\
                    + static(settings.INDOOR_AREAS_URL, document_root=settings.INDOOR_AREAS_ROOT) \
                    + static(settings.UPDADTER_PRIKAZ_URL, document_root=settings.UPDADTER_PRIKAZ_ROOT)

custom_admin_urls = (
    path('admin/main/schools/export/', export, name="export"),
    path('admin/main/schools/update/', update, name="update"),
    path('admin/main/schools/imp/', imp, name="import")
)

urlpatterns = [
    path('back-end/', include(extra_urlpatterns)),
    path('admin/', admin.site.urls, name='admin'),
    path('', include(extra_urlpatterns))
]

urlpatterns += custom_admin_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.DOCUMENT_URL, document_root=settings.DOCUMENT_ROOT)
# urlpatterns += static(settings.DOCUMENT_ROOT, document_root=settings.DOCUMENT_ROOT)