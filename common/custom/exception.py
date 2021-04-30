# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/23 5:38 下午 
# @Author : wangHua
# @File : exception.py 
# @Software: PyCharm


from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    return response
