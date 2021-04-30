# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/29 1:51 下午
# @Author : wangHua
# @File : serializer.py
# @Software: PyCharm

from .base import *
from rest_framework import serializers


class ResourceSerializer(BaseResourceSerializer):
    pass


class JobRelationSerializer(BaseJobRelationSerializer):
    pass


class UploaderSerializer(BaseUploaderSerializer):
    pass


class VideoSerializer(BaseVideoSerializer):
    download = serializers.BooleanField(write_only=True, default=False)
    uploader = BaseUploaderSerializer(read_only=True)
    video_resource = BaseResourceSerializer(read_only=True)
    thumbnail_resource = BaseResourceSerializer(read_only=True)
    task_id = serializers.CharField(read_only=True)
    task_progress = serializers.JSONField(read_only=True)
    video_format_set = BaseVideoFormatSerializer(many=True, read_only=True)
    video_thumbnail_set = BaseVideoThumbnailSerializer(many=True, read_only=True)


class VideoFormatSerializer(BaseVideoFormatSerializer):
    video = BaseVideoSerializer(read_only=True)
    video_id = serializers.CharField(allow_null=True)


class VideoThumbnailSerializer(BaseVideoThumbnailSerializer):
    video = BaseVideoSerializer(read_only=True)
    video_id = serializers.CharField(allow_null=True)


class KeywordSerializer(BaseKeywordSerializer):
    count = serializers.IntegerField(write_only=True, default=10)
