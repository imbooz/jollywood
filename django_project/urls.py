"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import UserProfileView, UserProfileEditView
from user import views as user_views

urlpatterns = [
    path('', include('jollywood.urls')),
    path('cpanel/', admin.site.urls),
    path('register/', user_views.register, name='user-register'),
    path('profile/', user_views.redirector, name='user-redirect-to-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', extra_context={'title': 'Log In'}), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html', extra_context={'title': 'Log Out'}), name='user-logout'),
    path('<slug>/', UserProfileView.as_view(), name='user-profile'),
    path('<slug>/edit', UserProfileEditView.as_view(), name='user-profile-edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)