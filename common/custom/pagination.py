# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/24 4:12 下午 
# @Author : wangHua
# @File : pagination.py
# @Software: PyCharm

from rest_framework.response import Response
from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination


class CustomPaginationOrderDict(OrderedDict):
    pass


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'pageSize'  # items per page
    page_query_param = 'current'  # items per page

    def get_paginated_response(self, data):
        return Response(CustomPaginationOrderDict([
            ('total', self.page.paginator.count),
            ('data', data),
        ]))
