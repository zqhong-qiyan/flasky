# -*- coding:utf-8 -*-
"""
@author:zhouqiuhong
@file:__init__.py.py
@time:2019/2/21 002115:14
"""
from flask import Blueprint

main = Blueprint("main", __name__)

from . import views, errors
