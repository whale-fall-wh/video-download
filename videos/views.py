# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/28 10:05 上午
# @Author : wangHua
# @File : views.py
# @Software: PyCharm

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="接口文档",
      default_version='v1',
      description="使用youtube-dl 下载视频",
      contact=openapi.Contact(email="wh970305@163.com"),
   ),
   public=True,
)
