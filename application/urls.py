from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='media_home'),
    path ('about/', views.about, name='media_about'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)