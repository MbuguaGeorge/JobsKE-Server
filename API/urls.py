from . import views
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('register', views.register, name=('register')),
    path('profile', views.create_profile, name=('profile')),
    path('login', views.TokenView.as_view()),
    path('org', views.org_profile, name=('org')),
    path('post', views.jobpost, name=('post')),
    path('organizations', views.Organizations.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)