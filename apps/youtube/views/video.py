# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/21 3:48 下午 
# @Author : wangHua
# @File : video.py 
# @Software: PyCharm

from rest_framework import status, viewsets
from rest_framework.response import Response

from ..tasks import download_video, search_keyword
from ..serializers import *
from ..filters import *
from ..repositories import JobRelationRepository


# ViewSets define the view behavior.
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    job_repository = JobRelationRepository()
    filterset_class = VideoFilter
    ordering_fields = ('id', 'view_count')
    ordering = ['-id']

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        video_id = ser.validated_data.get('video_id')
        download = ser.validated_data.get('download')
        video = Video.objects.filter(video_id=video_id).first()
        task_id = download_video.delay(
            video_id,
            download=download
        ).task_id
        if video and download:
            self.job_repository.save(model=Video.task_type(), model_id=video.id, task_id=task_id)

        return Response(ser.validated_data, status=status.HTTP_201_CREATED)


# ViewSets define the view behavior.
class VideoFormatViewSet(viewsets.ModelViewSet):
    queryset = VideoFormat.objects.all()
    serializer_class = VideoFormatSerializer


# ViewSets define the view behavior.
class VideoThumbnailViewSet(viewsets.ModelViewSet):
    queryset = VideoThumbnail.objects.all()
    serializer_class = VideoThumbnailSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        keyword = ser.validated_data.get('keyword')
        count = ser.validated_data.get('count')
        Keyword.objects.update_or_create(keyword=keyword)

        search_keyword.delay(keyword=keyword, count=count)

        return Response(ser.data, status=status.HTTP_201_CREATED)
