from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('', include('DjangoHUDApp.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = 'DjangoHUDApp.views.handler404'