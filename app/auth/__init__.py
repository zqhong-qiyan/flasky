# -*- coding:utf-8 -*-
"""
@author:zhouqiuhong
@file:__init__.py.py
@time:2019/2/21 002117:10
"""
from flask import Blueprint

auth = Blueprint("auth", __name__)

from . import views