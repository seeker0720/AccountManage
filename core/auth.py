#!/usr/bin/env python3
# coding=utf-8

"""
@File：auth.py
@Author：seeker0720
@Date：2019/10/7 19:20
@Instructions:
"""
from core.models import create_session, LoginMsg
from core.common import md5_msg


Session = create_session()


def log_inner(func):
    def wrapper(*args, **kwargs):
        error_num = 0
        while error_num < 5:
            error_num += 1
            tips = f'{error_num:-^20}'
            print(tips)
            login_name = input('登录名：').strip()
            login_password_tmp = input('登陆密码：').strip()

            obj = Session.query(LoginMsg).filter_by(login_name=login_name).first()

            if not obj:
                print('用户不存在')
            else:
                if obj.login_password == md5_msg(login_password_tmp):
                    print(f'{login_name} 登录成功')
                    return func(*args, **kwargs)
                else:
                    print('密码错误')
        else:
            print('错误次数太多，请稍后')
    return wrapper


def login():
    Session = create_session()
    error_num = 0
    login_status = 0
    while error_num < 5:
        error_num += 1
        tips = f'{error_num:-^20}'
        print(tips)
        login_name = input('登录名：').strip()
        login_password_tmp = input('登陆密码：').strip()

        obj = Session.query(LoginMsg).filter_by(login_name=login_name).first()

        if not obj:
            print('用户不存在')
        else:
            if obj.login_password == md5_msg(login_password_tmp):
                print(f'{login_name} 登录成功')
                login_status = 1
                return obj.id, login_status
            else:
                print('密码错误')
    else:
        print('错误次数太多，请稍后')
        return None, login_status


if __name__ == '__main__':
    login_name1, login_status1 = login()
    print(login_name1, login_status1)
