# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 10:10 上午
# @Author : wangHua
# @File : youtube_dl.py
# @Software: PyCharm

import youtube_dl
from django.conf import settings


class YoutubeDownload(object):
    def __init__(self):
        self._ydl_opts = {
            'outtmpl': '{}/videos/%(extractor)s/%(id)s/%(format_id)s-%(format_note)s.%(ext)s'.format(
                settings.MEDIA_ROOT
            ),
        }

    def set_proxy(self, proxy):
        return self.add_opt('proxy', proxy)

    def set_opt(self, ydl_opts: dict):
        self._ydl_opts.update(ydl_opts)
        return self

    def add_opt(self, key, value):
        self._ydl_opts[key] = value
        return self

    def download(self, url, download: bool = False):
        with youtube_dl.YoutubeDL(self._ydl_opts) as ydl:
            result = ydl.extract_info(
                url,
                download=download
            )

        return result
