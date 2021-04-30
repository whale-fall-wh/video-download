"""videos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static   # static 助手函数只有在debug=True时才生效，生产环境请使用nginx来配置
from .views import schema_view


urlpatterns = [
    url('swagger', schema_view.with_ui(), name='schema-swagger-ui'),
    path('api/celery-result/', include('django_celery_results.urls')),
    # path('accounts/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/youtube/', include('apps.youtube.urls')),
    path('api/auth/', include('apps.user.urls')),
    path('api/admin/', include('rest_framework.urls', namespace='rest_framework'))
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
