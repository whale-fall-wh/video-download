# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/24 4:13 下午
# @Author : wangHua
# @File : __init__.py.py
# @Software: PyCharm

from abc import abstractmethod, ABCMeta


class CustomRepository(metaclass=ABCMeta):

    def __init__(self):
        self.objects = self.init_model().objects

    @abstractmethod
    def init_model(self):
        pass

    def __getattr__(self, key):
        def not_find(*args, **kwargs):
            return getattr(self.init_model(), key)(*args, **kwargs)
        return not_find
