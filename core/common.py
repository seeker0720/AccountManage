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
from core import models
from conf.settings import ADMINISTRATOR, WARNING
from core import admin


def md5_msg(args):
    msg = args
    hl = hashlib.md5()
    hl.update(msg.encode())
    new_msg = hl.hexdigest()
    return new_msg


def welcome(func):
    def wrapper(*args, **kwargs):
        print('欢迎使用AccountManage')
        func(*args, **kwargs)
        print('Bye')
    return wrapper


def table_header(func):
    def wrapper(*args, **kwargs):
        column_a = '|USER_ID'
        column_b = '|USER_NAME'
        column_c = '|USER_TYPE'
        column_d = '|USER_PASSWORD'
        print(f'{column_a:<10}{column_b:<21}{column_d:<21}{column_c}')
        return func(*args, **kwargs)
    return wrapper


def logger_a(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        msg = 'Well Done'
        print(f'{msg:-^20}')
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
            Session = models.create_session()
            obj = Session.query(models.LoginMsg).filter_by(login_name=name).first()
            _password = obj.login_password
            error_num = 0
            while error_num < 3:
                error_num += 1
                tips = f'{error_num:-^20}'
                print(tips)
                password = input('请输入管理员密码：').strip()
                if _password == md5_msg(password):
                    return func(*args, **kwargs)
                else:
                    print('密码错误')
            else:
                print('错误次数太多!!!')
        return inner
    return wrapper


def get_account_obj_list():
    Session = models.create_session()
    obj = Session.query(models.LoginMsg).filter_by(login_name=ADMINISTRATOR).first()
    obj_account_list = obj.account_msg
    return obj_account_list


@table_header
def get_account_obj():
    account_obj_ls = get_account_obj_list()
    if account_obj_ls:
        for account_obj in account_obj_ls:
            user_id, user_type, user_name = admin.AdminModels(obj=account_obj,
                                                              session=models.create_session()).view_simple_msg()
            user_password = '******'
            account_simple_msg = f'|{user_id:<9}|{user_name:<20}|{user_password:<20}|{user_type}'
            print(account_simple_msg)
        return 1
    else:
        warning = WARNING[1]
        print(f'\n{warning:-^60}\n')
        return 0


@table_header
def output_detail_msg(user_id, user_name, user_password, user_type):
    account_simple_msg = f'|{user_id:<9}|{user_name:<20}|{user_password:<20}|{user_type}'
    print(account_simple_msg)


def options():
    option_list = [
        '查询信息',
        '添加信息',
        '修改信息',
        '删除信息'
    ]
    for index, option in enumerate(option_list):
        print(index+1, option)


def tips():
    print('\n<使用 回车键 确认，q或Q 退出程序>')


if __name__ == '__main__':
    pass

