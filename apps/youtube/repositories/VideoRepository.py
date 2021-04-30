# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 4:22 下午
# @Author : wangHua
# @File : VideoRepository.py
# @Software: PyCharm

from common.custom.repository import CustomRepository
from ..models import Video
from ..entities import VideoEntity


class VideoRepository(CustomRepository):
    def init_model(self):
        return Video

    def save_by_entity(self, entity: VideoEntity):
        data = entity.only(['title', 'title', 'description', 'upload_date', 'uploader_id', 'channel_id',
                            'duration', 'view_count', 'average_rating', 'age_limit', 'like_count', 'dislike_count'])
        video, flag = self.objects.update_or_create(**entity.only(['video_id']), defaults=data)

        return video
