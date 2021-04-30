# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/23 5:38 下午 
# @Author : wangHua
# @File : renderer.py
# @Software: PyCharm

# 导入控制返回的JSON格式的类
from rest_framework.renderers import JSONRenderer

from .status import *
from .pagination import CustomPaginationOrderDict


class CustomRenderer(JSONRenderer):
    # 重构render方法
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            if isinstance(data, dict):
                msg = data.pop('message', 'success')
            else:
                msg = 'success'
            if isinstance(data, CustomPaginationOrderDict):
                # 如果是分页类型的，统一直接返回
                data['message'] = msg
                return super().render(data, accepted_media_type, renderer_context)

            # 重新构建返回的JSON字典
            for key in data:
                # 判断是否有自定义的异常的字段
                if key == 'message':
                    msg = data[key]
                    data = None
            ret = {
                'message': msg,
                'data': data,
            }
            # 返回JSON数据
            return super().render(ret, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)
