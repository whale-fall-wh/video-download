# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 4:33 下午
# @Author : wangHua
# @File : VideoService.py
# @Software: PyCharm

from ..repositories import *
from ..entities import VideoEntity


class VideoService(object):
    uploaderRepository = UploaderRepository()
    resourceRepository = ResourceRepository()
    videoRepository = VideoRepository()
    videoFormatRepository = VideoFormatRepository()
    videoThumbnailRepository = VideoThumbnailRepository()

    def save_by_entity(self, entity: VideoEntity, save_resource=False):
        uploader = self.uploaderRepository.save_by_entity(entity.upload_entity)
        format_resource = None
        video = self.videoRepository.save_by_entity(entity)
        if save_resource:
            format_resource = self.resourceRepository.save_video_resource(entity)
            format_resource and format_resource.video_resource_set.add(video)
        uploader.video_set.add(video)
        for format_entity in entity.formats:
            video_format = self.videoFormatRepository.save_by_entity(format_entity)
            if save_resource and format_resource and format_entity.format_id == entity.format_id:
                format_resource.video_format_resource_set.add(video_format)
            video.video_format_set.add(video_format)

        for thumbnail_entity in entity.thumbnails:
            video_thumbnail = self.videoThumbnailRepository.save_by_entity(thumbnail_entity)
            video.video_thumbnail_set.add(video_thumbnail)
            if thumbnail_entity.filename:
                thumbnail_resource = self.resourceRepository.save_thumbnail_resource(thumbnail_entity)
                thumbnail_resource and thumbnail_resource.thumbnail_resource_set.add(video)
                thumbnail_resource and thumbnail_resource.video_thumbnail_resource_set.add(video_thumbnail)

        return video
