from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

version = '0.1.2'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('client.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('en/', include(('home.urls', 'home_en',))),
    path('', include(('home.urls', 'home',))),
]

# Media url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# DJDT
if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns
