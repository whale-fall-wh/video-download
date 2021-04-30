# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/29 1:48 下午
# @Author : wangHua
# @File : base.py
# @Software: PyCharm
"""
BaseSerializer 为了解决相互调用的问题
"""
from rest_framework import serializers
from ..models import *


class BaseUploaderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Uploader
        fields = "__all__"


class BaseResourceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Resource
        fields = "__all__"


class BaseJobRelationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = JobRelation
        fields = "__all__"


class BaseVideoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    video_id = serializers.CharField(required=True, error_messages={'required': '视频ID不能为空'})

    class Meta:
        model = Video
        fields = '__all__'


class BaseVideoThumbnailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    resource = BaseResourceSerializer(read_only=True)
    resource_id = serializers.IntegerField(write_only=True, allow_null=True)

    class Meta:
        model = VideoThumbnail
        fields = "__all__"


class BaseVideoFormatSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    resource = BaseResourceSerializer(read_only=True)
    resource_id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = VideoFormat
        fields = "__all__"


class BaseKeywordSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    keyword = serializers.CharField(required=True, error_messages={'required': '关键字不能为空'})
    video_set = BaseVideoSerializer(read_only=True)

    class Meta:
        model = Keyword
        fields = "__all__"
