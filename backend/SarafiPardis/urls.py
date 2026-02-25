"""
URL configuration for SarafiPardis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView

from . import views

# Set custom 404 handler
handler404 = views.handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', views.favicon_view, name='favicon'),
    path("api/", include("SarafiPardis.api_urls")),
    path('landingpage/', include('landing.urls', namespace='landing')),
    path('landing/', RedirectView.as_view(pattern_name='landing:home', permanent=True)),
    path("template-editor/", include("template_editor.frontend_urls", namespace="template_editor_frontend")),
    path("", include("accounts.urls", namespace="accounts")),
    re_path(r'^.*$', views.SPAView.as_view(), name='spa'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
