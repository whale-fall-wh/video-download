# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 4:05 下午
# @Author : wangHua
# @File : entity.py
# @Software: PyCharm

from abc import ABCMeta
from copy import deepcopy


class CustomEntity(metaclass=ABCMeta):

    def __init__(self):
        pass

    @classmethod
    def instance(cls, data: dict):
        return cls().to_object(data=data)

    def to_object(self, data: dict):
        for k, v in data.items():
            if hasattr(self, k):
                setattr(self, k, v)

        return self

    def only(self, keys: list) -> dict:
        data = self.__dict__

        return {key: value for key, value in data.items() if key in keys}

    def besides(self, keys: list) -> dict:
        data = deepcopy(self).__dict__
        [data.pop(k) for k in keys]

        return data
