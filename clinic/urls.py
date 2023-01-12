
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static 

from django.views.static import serve 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_dashboard.urls')),
    path('', include('appointment.urls')),
    path('', include('inventory.urls')),
    path('', include('authentication.urls')),
]


#handler404 = "admin_dashboard.views.page_not_found_view"

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
