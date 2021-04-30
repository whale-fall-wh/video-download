# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/21 2:25 下午 
# @Author : wangHua
# @File : uploader.py 
# @Software: PyCharm
from rest_framework import viewsets
from rest_framework.response import Response
from ..models import Uploader
from ..serializers import UploaderSerializer
from rest_framework.decorators import action
from ..filters import UploaderFilter


# ViewSets define the view behavior.
class UploaderViewSet(viewsets.ModelViewSet):
    queryset = Uploader.objects.all()
    serializer_class = UploaderSerializer
    filterset_class = UploaderFilter

    # 自定义方法
    @action(methods=['get', 'post'], detail=False, url_path='user_action')
    def user_action(self, request, *args, **kwargs):
        dd = {"w": "ww", "ee": "ttt", "message": '123'}
        return Response(dd)
