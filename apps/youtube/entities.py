# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 4:14 下午
# @Author : wangHua
# @File : entities.py
# @Software: PyCharm

from common.custom.entity import CustomEntity
from copy import deepcopy
from datetime import datetime


class UploaderEntity(CustomEntity):
    uploader_id = ''
    uploader = ''
    uploader_url = ''


class VideoFormatEntity(CustomEntity):
    video_id = ''
    format_id = ''
    asr = 0
    filesize = 0
    format_note = ''
    fps = 0
    height = 0
    width = 0
    quality = 0
    ext = ''


class VideoThumbnailEntity(CustomEntity):
    video_id = ''
    thumbnail_id = ''
    width = 0
    height = 0
    filename = ''

    def to_object(self, data: dict):
        super(VideoThumbnailEntity, self).to_object(data)
        self.thumbnail_id = data.get('id', '')

        return self


class VideoEntity(CustomEntity):
    video_id = ''  # 视频ID
    title = ''  # 视频标题
    formats = None
    thumbnails = None  # 缩略图
    description = ''  # 描述
    upload_date = ''  # 上传时间
    upload_entity = None
    uploader = ''  # 作者
    uploader_id = ''
    uploader_url = ''  # 作者主页
    channel_id = ''  # 频道
    channel_url = ''  # 频道地址
    duration = 0  # 时长
    view_count = 0  # 播放次数
    average_rating = 0.0  # 平均评分
    age_limit = 0  # 年龄限制
    webpage_url = ''  #
    categories = None
    tags = None
    is_live = None
    subtitles = None
    like_count = 0
    dislike_count = 0
    channel = ''
    extractor = ''
    webpage_url_basename = ''
    extractor_key = ''
    playlist = None
    playlist_index = None
    thumbnail = ''
    display_id = ''
    requested_subtitles = ''
    asr = 0
    filesize = 0
    format_id = ''
    format_note = ''
    fps = 0
    height = 0
    quality = 0
    tbr = 0.0
    url = ''
    width = 0
    ext = ''
    vcodec = ''
    acodec = ''
    format = ''
    protocol = ''
    http_headers = ''

    def to_object(self, data: dict):
        super(VideoEntity, self).to_object(data)
        self.video_id = data.get('id', '')
        if self.upload_date:
            upload_date = datetime.strptime(self.upload_date, '%Y%m%d')
            self.upload_date = upload_date.strftime('%Y-%m-%d')
        formats = deepcopy(self.formats)
        self.formats = []
        if formats and type(formats) == list:
            for formatItem in formats:
                if type(formatItem) == dict:
                    formatItem['video_id'] = self.video_id
                    self.formats.append(VideoFormatEntity.instance(formatItem))

        thumbnails = deepcopy(self.thumbnails)
        self.thumbnails = []
        if thumbnails and type(thumbnails) == list:
            for thumbnailItem in thumbnails:
                if type(thumbnailItem) == dict:
                    thumbnailItem['video_id'] = self.video_id
                self.thumbnails.append(VideoThumbnailEntity.instance(thumbnailItem))

        self.upload_entity = UploaderEntity.instance(self.only(['uploader', 'uploader_id', 'uploader_url']))

        return self


class VideoListEntity(CustomEntity):
    _type = 'playlist'
    entries = None
    videos = []

    def to_object(self, data: dict):
        super(VideoListEntity, self).to_object(data)

        if self.entries and type(self.entries) == list:
            for entry in self.entries:
                self.videos.append(VideoEntity.instance(entry))

        return self
