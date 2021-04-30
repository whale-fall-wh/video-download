# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 4:23 下午
# @Author : wangHua
# @File : VideoFormatRepository.py
# @Software: PyCharm

from common.custom.repository import CustomRepository
from ..models import VideoFormat
from ..entities import VideoFormatEntity


class VideoFormatRepository(CustomRepository):
    def init_model(self):
        return VideoFormat

    def save_by_entity(self, entity: VideoFormatEntity):
        data = entity.besides(['video_id', 'format_id'])
        video_format, flag = self.objects.update_or_create(**entity.only(['video_id', 'format_id']), defaults=data)

        return video_format
