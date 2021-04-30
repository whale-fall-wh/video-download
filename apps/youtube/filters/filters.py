# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/29 2:24 下午
# @Author : wangHua
# @File : filters.py
# @Software: PyCharm

import django_filters
from django_filters import rest_framework
from ..models import *


class UploaderFilter(django_filters.FilterSet):
    uploader = rest_framework.CharFilter(field_name='uploader', lookup_expr='contains')
    uploader_id = rest_framework.CharFilter(field_name='uploader_id')

    class Meta:
        model = Uploader
        fields = ['uploader', 'uploader_id']


class VideoFilter(django_filters.FilterSet):
    uploader_id = rest_framework.CharFilter(field_name='uploader_id')
    uploader = rest_framework.CharFilter(field_name='uploader__uploader', lookup_expr='contains')
    title = rest_framework.CharFilter(field_name='title', lookup_expr='contains')

    class Meta:
        model = Video
        fields = ['title', 'uploader_id', 'uploader']
