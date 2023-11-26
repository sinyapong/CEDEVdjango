from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from book.api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('myapp.urls','myapp'), namespace='myapp')),
    path('book/', include(('book.urls','book'), namespace='book')),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
