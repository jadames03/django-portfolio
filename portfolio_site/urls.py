from django.contrib import admin
from django.urls import path, include
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', views.home, name="home"),
    # path('about/', views.about, name='about'),
    path('debug-media/', views.debug_media, name='debug-media'),
]

# These are not needed if using serve view
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
