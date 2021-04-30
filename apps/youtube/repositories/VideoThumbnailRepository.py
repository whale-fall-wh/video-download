# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 4:24 下午
# @Author : wangHua
# @File : VideoThumbnailRepository.py
# @Software: PyCharm

from common.custom.repository import CustomRepository
from ..models import VideoThumbnail
from ..entities import VideoThumbnailEntity


class VideoThumbnailRepository(CustomRepository):
    def init_model(self):
        return VideoThumbnail

    def save_by_entity(self, entity: VideoThumbnailEntity) -> VideoThumbnail:
        video_thumbnail, flag = self.objects.update_or_create(
            **entity.only(['video_id', 'thumbnail_id']),
            defaults=entity.only(["height", "width", "resolution"])
        )

        return video_thumbnail
