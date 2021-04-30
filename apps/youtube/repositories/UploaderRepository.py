# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 4:21 下午
# @Author : wangHua
# @File : UploaderRepository.py
# @Software: PyCharm

from common.custom.repository import CustomRepository
from ..models import Uploader
from ..entities import UploaderEntity


class UploaderRepository(CustomRepository):
    def init_model(self):
        return Uploader

    def save_by_entity(self, entity: UploaderEntity):
        uploader, flag = self.objects.update_or_create(
            **entity.only(['uploader_id']),
            defaults=entity.besides(['uploader_id'])
        )

        return uploader
