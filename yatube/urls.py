"""yatube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.contrib.flatpages import views


urlpatterns = [
    path('about/', include('django.contrib.flatpages.urls')),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),

]

urlpatterns += [
        path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
        path('terms/', views.flatpage, {'url': '/terms/'}, name='terms'),
        path('about-author/', views.flatpage, {'url': '/about-author/'}, name='about'),
        path('about-spec/', views.flatpage, {'url': '/about-spec/'}, name='terms'),
        path("", include("posts.urls")),
]