# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/21 2:37 下午 
# @Author : wangHua
# @File : models.py
# @Software: PyCharm

from django.db import models


class UnsignedIntegerField(models.IntegerField):
    def db_type(self, connection):
        return 'integer UNSIGNED'


class UnsignedBigIntegerField(models.BigIntegerField):
    def db_type(self, connection):
        return 'bigint UNSIGNED'


class UnsignedAutoBigIntegerField(models.BigAutoField):
    def db_type(self, connection):
        return 'bigint UNSIGNED AUTO_INCREMENT'
