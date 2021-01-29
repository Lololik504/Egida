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
                    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

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
