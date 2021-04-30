# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 9:47 上午
# @Author : wangHua
# @File : ResourceRepository.py
# @Software: PyCharm

from common.custom.repository import CustomRepository
from ..models import Resource
from ..entities import VideoEntity, VideoThumbnailEntity
from django.conf import settings


class ResourceRepository(CustomRepository):
    def init_model(self):
        return Resource

    def save_video_resource(self, entity: VideoEntity, resource_type: int = 1) -> Resource:
        # ydl没有返回视频地址，这边需要自己拼接
        video_path = '{video_path}/videos/{extractor}/{id}/{format}-{format_note}.{ext}'.format(**{
            'video_path': settings.MEDIA_ROOT,
            'extractor': entity.extractor,
            'id': entity.video_id,
            'format': entity.format_id,
            'format_note': entity.format_note,
            'ext': entity.ext
        }).replace(settings.BASE_DIR.__str__(), '')
        resource, flag = self.objects.update_or_create(**{'path': video_path}, defaults={'type': resource_type})

        return resource

    def save_thumbnail_resource(self, entity: VideoThumbnailEntity, resource_type: int = 1) -> Resource:
        # ydl返回了封面地址，直接解析一下就行
        thumbnail_path = entity.filename.replace(settings.BASE_DIR.__str__(), '')
        resource, flag = self.objects.update_or_create(**{'path': thumbnail_path}, defaults={'type': resource_type})

        return resource
