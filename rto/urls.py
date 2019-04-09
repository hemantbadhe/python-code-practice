from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rto_app import views

urlpatterns = [
    url(r'^$/', views.user_login, name='user_login'),
    url(r'^', include('rto_app.urls')),
    url(r'^admin/', admin.site.urls),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)