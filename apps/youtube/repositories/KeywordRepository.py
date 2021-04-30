# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/30 2:36 下午
# @Author : wangHua
# @File : KeywordRepository.py
# @Software: PyCharm
from common.custom.repository import CustomRepository
from ..models import Keyword


class KeywordRepository(CustomRepository):
    def init_model(self):
        return Keyword
