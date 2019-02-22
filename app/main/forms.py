# -*- coding:utf-8 -*-
"""
@author:zhouqiuhong
@file:forms.py
@time:2019/2/21 002115:15
"""
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField("what's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

