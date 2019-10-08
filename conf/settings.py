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
        'USER': 'admin',
        'PASSWORD': 'AccountManage123!@#',
        'HOST': 'localhost',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


default_DB = DATABASES.get('default')
ENGINE = f"{default_DB.get('DB_API')}://{default_DB.get('USER')}:{default_DB.get('PASSWORD')}@{default_DB.get('HOST')}/{default_DB.get('NAME')}?charset=utf8mb4"


ERROR = [
    'Error：输入错误',
    'Error：账户信息不存在',
    'Error：请输入数字'
    'Error：用户不存在'
]

WARNING = [
    'Warning：错误次数太多',
    'Warning：无用户信息，请添加信息后再执行该操作',
    'Warning：错误次数太多',
    'Warning：密码错误'

]
