from . import views
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('register', views.register, name=('register')),
    path('login', views.TokenView.as_view()),

    path('profile', views.create_profile, name=('profile')),
    path('org', views.org_profile, name=('org')),

    path('post', views.jobpost, name=('post')),
    path('jobs', views.Jobs.as_view()),
    path('joblist', views.JobsView.as_view()),
    path('joblist/<slug:slug>/', views.JobPosts.as_view()),
    path('proposal/<slug:slug>/', views.proposal, name=('proposal')),

    path('user', views.UserProfileView.as_view()),
    path('cur', views.CurUser.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)