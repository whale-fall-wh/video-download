# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/26 9:59 上午 
# @Author : wangHua
# @File : task.py 
# @Software: PyCharm

from abc import ABC
import celery


class CustomTask(celery.Task, ABC):
    # 任务失败时执行
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    # 任务成功时执行
    def on_success(self, retval, task_id, args, kwargs):
        pass

    # 任务重试时执行
    def on_retry(self, exc, task_id, args, kwargs, einfo):
        pass
