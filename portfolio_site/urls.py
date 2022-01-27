from django.contrib import admin
from django.urls import path, include
from quote_generator import views as quoteView
from exchange_rate import views as exchangeView
from portfolio import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quote_generator', quoteView.index, name='index'),
    path('exchange_rate/', exchangeView.index, name='index'),
    path('blog/', include('blog.urls')),
    path('', views.home, name="home"),
    # path('about/', views.about, name='about'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
