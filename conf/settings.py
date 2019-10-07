#!/usr/bin/env python3
# coding=utf-8

"""
@File：settings.py
@Author：seeker0720
@Date：2019/10/7 18:54
@Instructions:
"""
ADMINISTRATOR = 'Admin'

DATABASES = {
    'default': {
        'DB_API': 'mysql+pymysql',
        'NAME': 'accountdb',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


default_DB = DATABASES.get('default')
ENGINE = f"{default_DB.get('DB_API')}://{default_DB.get('USER')}:{default_DB.get('PASSWORD')}@{default_DB.get('HOST')}/{default_DB.get('NAME')}?charset=utf8"
