# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/23 12:09 下午 
# @Author : wangHua
# @File : urls.py 
# @Software: PyCharm

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.user import views


urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('info', views.info)
]
