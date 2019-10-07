#!/usr/bin/env python3
# coding=utf-8

"""
@File：common.py
@Author：seeker0720
@Date：2019/10/7 18:53
@Instructions:
"""

import hashlib
import time
from core.models import LoginMsg, create_session
from conf.settings import ADMINISTRATOR


def md5_msg(args):
    msg = args
    hl = hashlib.md5()
    hl.update(msg.encode())
    new_msg = hl.hexdigest()
    return new_msg


def logger(func):
    def wrapper(*args, **kwargs):
        print('欢迎使用AccountManage')
        func(*args, **kwargs)
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        cost_time = end_time - start_time
        print(f'用时：{cost_time}')
    return wrapper


def auth_password(name=ADMINISTRATOR):
    def wrapper(func):
        def inner(*args, **kwargs):
            Session = create_session()
            obj = Session.query(LoginMsg).filter_by(login_name=name).first()
            _password = obj.login_password
            error_num = 0
            while error_num < 3:
                error_num += 1
                tips = f'{error_num:-^20}'
                print(tips)
                password = input('输入密码确认').strip()
                if _password == md5_msg(password):
                    return func(*args, **kwargs)
                else:
                    print('密码错误')
            else:
                print('错误次数太多!!!')
        return inner
    return wrapper


if __name__ == '__main__':
    pass
