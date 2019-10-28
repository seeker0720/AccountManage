#!/usr/bin/env python3
# coding=utf-8

"""
@File：auth.py
@Author：seeker0720
@Date：2019/10/7 19:20
@Instructions:
"""
import getpass
from core.models import create_session, LoginMsg
from core.common import md5_msg
from conf.settings import WARNING,ERROR

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
                    warning = WARNING[3]
                    print(f'\n{warning:-^60}\n')
        else:
            warning = WARNING[0]
            print(f'\n{warning:-^60}\n')
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
            error = ERROR[3]
            print(f'\n{error:!^40}\n')
        else:
            if obj.login_password == md5_msg(login_password_tmp):
                print(f'{login_name} 登录成功')
                login_status = 1
                return obj.id, login_status
            else:
                warning = WARNING[3]
                print(f'\n{warning:-^60}\n')
    else:
        warning = WARNING[0]
        print(f'\n{warning:-^60}\n')
        return None, login_status


def auth_password(name):
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
                #password = input('请输入管理员密码：').strip()
                password = getpass.getpass('请输入管理员密码：')
                if _password == md5_msg(password):
                    return func(*args, **kwargs)
                else:
                    warning = WARNING[3]
                    print(f'\n{warning:-^60}\n')
            else:
                warning = WARNING[0]
                print(f'\n{warning:-^60}\n')
        return inner
    return wrapper


if __name__ == '__main__':
    # login_name1, login_status1 = login()
    # print(login_name1, login_status1)
    pass
