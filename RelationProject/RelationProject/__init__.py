#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 22:02
# @Author  : rain
# @File    : logger.py
# @Software: PyCharm

from flask import Flask,Blueprint
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import re_config

app = Flask(__name__)

app.static_folder = re_config.STATIC_FLODER
app.template_folder = re_config.TEMPLATE_FLODER
app.secret_key = '123456'
app.config.from_object(re_config)
db = SQLAlchemy(app)
"""
    migrate 与 manger 的作用是让，主程序和模型类分离
"""
#初始化mirate 对象绑定app和db
migrate = Migrate(app,db)
manager =Manager(app)
#把migratecommand命令添加到manager中,db为自定义的名称
manager.add_command('db',MigrateCommand)


def register_blueprint_models():
    try:
        from RelationProject.views import BLUEPRINT_MODELS
        if not isinstance(BLUEPRINT_MODELS, (tuple, list, set)):
            raise AssertionError('BLUEPRINT_MODELS must be (tuple, list, set) type.')
    except (ImportError,AssertionError) as e:
        print(e)
        return

    for model in BLUEPRINT_MODELS:
        if not isinstance(model,Blueprint):
            continue
        try:
            app.register_blueprint(model)
        except Exception as e:
            print(e)

def __init_tables():
    db.create_all()


register_blueprint_models()
__init_tables()