#!/usr/bin/env python3
# coding=utf-8

"""
@File：admin.py
@Author：seeker0720
@Date：2019/10/8 0:17
@Instructions:
"""
from core.models import LoginMsg, PasswordCase, create_session
from core.auth import login
from conf.settings import ADMINISTRATOR
from core.common import md5_msg


class AdminModels:

    Session = create_session()
    name = ADMINISTRATOR

    def __init__(self, password):
        self.password = password

    def create_admin_account(self):

        obj = LoginMsg(login_name=self.name, login_password=md5_msg(self.password))
        find_obj = self.Session.query(LoginMsg).filter_by(login_name=self.name).first()
        # 避免创建重复的管理员账户
        if not find_obj:
            self.Session.add(obj)
        self.Session.commit()
        print('创建成功')

    def insert_msg(self):
        pass

    def delete_msg(self):
        pass

    def modify_msg(self):
        pass

    def view_msg(self):
        pass


if __name__ == '__main__':
    tmp = AdminModels(password='WWH072093')
    tmp.create_admin_account()
