# coding: utf-8

from flask import Flask

app = Flask(__name__)

# 通过配置文件家在
app.config.from_object('settings')

import settings
app.config.from_object(settings)


# 通过文件名字加载
app.config.from_pyfile('settings.py', silent=True)


# 通过环境变量加载
# export YOUTAPPLICATION_SETTINGS='settings.py'
app.config.from_envvar('YOURAPPLICATION_SETTINGS')