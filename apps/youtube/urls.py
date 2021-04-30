# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/21 2:24 下午 
# @Author : wangHua
# @File : urls.py 
# @Software: PyCharm

from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'uploader', UploaderViewSet)
router.register(r'video', VideoViewSet)
router.register(r'keyword', KeywordViewSet)
router.register(r'video-format', VideoFormatViewSet)
router.register(r'video-thumbnail', VideoThumbnailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
