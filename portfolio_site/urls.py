from django.contrib import admin
from django.urls import path, include
from portfolio import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', views.home, name="home"),
    # path('about/', views.about, name='about'),
    path('debug-media/', views.debug_media, name='debug-media'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Static files are handled by whitenoise
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)