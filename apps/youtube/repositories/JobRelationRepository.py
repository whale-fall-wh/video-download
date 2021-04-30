# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/27 5:55 下午
# @Author : wangHua
# @File : JobRelationRepository.py
# @Software: PyCharm

from common.custom.repository import CustomRepository
from ..models import JobRelation


class JobRelationRepository(CustomRepository):
    def init_model(self):
        return JobRelation

    def save(self, model, model_id, task_id):
        rs, flag = self.objects.update_or_create(model=model, model_id=model_id, defaults={"task_id": task_id})

        return rs
