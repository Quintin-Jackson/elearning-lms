from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import auth
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('', include('core.urls')),
    url(r'^admin/', admin.site.urls),
    ##### user related path##########################
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/', include('accounts.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
