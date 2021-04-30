# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/25 4:47 下午 
# @Author : wangHua
# @File : tasks.py 
# @Software: PyCharm

# @link https://blog.csdn.net/weixin_44649870/article/details/111867155, 关于任务执行结果的,celery自带的
#

from celery import shared_task
from common.custom.task import CustomTask
from common.utils.youtube_dl import YoutubeDownload
from .entities import VideoEntity, VideoListEntity
from .services import VideoService
from .models import Keyword, KeywordVideo

proxy = 'socks5://localhost:1080'

service = VideoService()


@shared_task(base=CustomTask)
def download_video(video_id, format_id=None, download: bool = False):
    ydl = YoutubeDownload().set_proxy(proxy)
    ydl.add_opt('writethumbnail', download).add_opt('noplaylist', True).add_opt('writeinfojson', True)
    format_id is not None and ydl.add_opt('format', format_id)
    result = ydl.download(
        f'https://www.youtube.com/watch?v={video_id}',
        download=download
    )
    video_entity = VideoEntity.instance(result)
    service.save_by_entity(video_entity, save_resource=download)
    return True


@shared_task(base=CustomTask)
def search_keyword(keyword: str, count: int = 10, download: bool = False):
    keyword_obj = Keyword.objects.get(keyword=keyword)
    ydl = YoutubeDownload().set_proxy(proxy)
    ydl.add_opt('noplaylist', True)
    result = ydl.download(
        f"ytsearch{count}:{keyword}",
        download=download
    )
    videos_entity = VideoListEntity.instance(result)
    for video_entity in videos_entity.videos:
        video = service.save_by_entity(video_entity, save_resource=download)
        KeywordVideo.objects.update_or_create(video=video, keyword=keyword_obj)

    return True
