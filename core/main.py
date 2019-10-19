#!/usr/bin/env python3
# coding=utf-8

"""
@File：main.py
@Author：seeker0720
@Date：2019/10/7 18:53
@Instructions:
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.admin import AdminLoginMsg as Al, AdminModels as Am, AdminAccount as Aa
from core.auth import auth_password
from conf.settings import ADMINISTRATOR, ERROR
from core import common, models


def create_password():
    password = input('设置管理员密码：').strip()
    al = Al(login_password=password)
    al.create_admin_account()


@common.welcome
@auth_password(name=ADMINISTRATOR)
def run():
    while True:
        common.options()
        common.tips()
        choice = input('请输入选项对应的数字(1～4)：').strip()
        if choice == 'q' or choice == 'Q':
            choice = '0'
        if not choice.isdigit():
            error = ERROR[0]
            print(f'\n{error:!^40}\n')
            continue
        if not int(choice) in range(5):
            error = ERROR[0]
            print(f'\n{error:!^40}\n')
            continue
        if choice == '1':
            # common.get_account_obj()
            if common.get_account_obj() == 0:
                continue
            user_id = input('选择对应的 USER_ID 查看全部信息：').strip()

            if user_id.isdigit():
                user_id = user_id
                session = models.create_session()
                obj = session.query(models.AccountMsg).filter_by(id=user_id).first()
                if not obj:
                    error = ERROR[1]
                    print(f'\n{error:!^40}\n')
                    continue
                try:
                    user_id, user_type, user_name, user_password = Am(obj=obj, session=session).view_detail_msg()
                except TypeError:
                    pass
                else:
                    common.output_detail_msg(user_id=user_id,
                                             user_name=user_name,
                                             user_password=user_password,
                                             user_type=user_type)
            else:
                error = ERROR[2]
                print(f'\n{error:!^40}\n')
        elif choice == '2':
            session = models.create_session()
            Aa(session=session).insert_msg()
        elif choice == '3':
            # common.get_account_obj()
            if common.get_account_obj() == 0:
                continue
            user_id = input('选择要修改信息的 USER_ID ：').strip()

            if user_id.isdigit():
                user_id = user_id
                session = models.create_session()
                obj = session.query(models.AccountMsg).filter_by(
                    id=user_id).first()
                if not obj:
                    error = ERROR[1]
                    print(f'\n{error:!^40}\n')
                    continue
                new_password = input('输入新的密码：').strip()
                if new_password:
                    Am(obj=obj, session=session).modify_password(new_password=new_password)
            else:
                error = ERROR[2]
                print(f'\n{error:!^40}\n')
        elif choice == '4':
            # common.get_account_obj()
            if common.get_account_obj() == 0:
                continue
            user_id = input('选择要删除信息的 USER_ID ：').strip()

            if user_id.isdigit():
                user_id = user_id
                session = models.create_session()
                obj = session.query(models.AccountMsg).filter_by(
                    id=user_id).first()
                if not obj:
                    error = ERROR[1]
                    print(f'\n{error:!^40}\n')
                    continue
                Am(obj=obj, session=session).delete_msg()
            else:
                error = ERROR[2]
                print(f'\n{error:!^40}\n')
        else:
            break

