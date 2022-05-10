from . import views
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('register', views.register, name=('register')),
    path('profile', views.create_profile, name=('profile')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)