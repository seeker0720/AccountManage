#!/usr/bin/env python3
# coding=utf-8

"""
@File：admin.py
@Author：seeker0720
@Date：2019/10/8 0:17
@Instructions:
"""
from core import models
from conf.settings import ADMINISTRATOR
from core.auth import auth_password
from core.common import md5_msg, logger_a


class TmpBase:
    Session = models.create_session()
    login_name = ADMINISTRATOR


class AdminLoginMsg:

    Session = models.create_session()
    login_name = ADMINISTRATOR

    def __init__(self, login_password):
        self.login_password = login_password

    @logger_a
    def create_admin_account(self):
        obj = models.LoginMsg(login_name=self.login_name,
                       login_password=md5_msg(self.login_password))
        find_obj = self.Session.query(models.LoginMsg).filter_by(
            login_name=self.login_name).first()
        # 避免创建重复的管理员账户
        if not find_obj:
            self.Session.add(obj)
            self.Session.commit()
        else:
            print('WARNING:管理员密码已设置，请不要重复设置')


class AdminAccount:
    login_name = ADMINISTRATOR

    def __init__(self, session):
        self.Session = session

    @logger_a
    def insert_msg(self):
        user_type = input('账户类型：').strip()
        user_name = input('账户登录名：').strip()
        user_password = input('账户密码：').strip()

        obj_login = self.Session.query(models.LoginMsg).filter_by(
            login_name=self.login_name).first()
        obj_account = models.AccountMsg(user_type=user_type,
                                        user_name=user_name,
                                        user_password=md5_msg(user_password),
                                        login_user_id=obj_login.id)
        obj_password = models.PasswordCase(password=user_password)
        self.Session.add(obj_account)
        find_obj = self.Session.query(models.PasswordCase).filter_by(
            password=user_password).first()
        # 避免创建重复的内容
        if not find_obj:
            self.Session.add(obj_password)
        self.Session.commit()



class AdminModels:

    login_name = ADMINISTRATOR

    def __init__(self, obj, session):
        self.obj = obj
        self.Session = session


    @logger_a
    def delete_msg(self):
        account_obj = self.obj
        self.Session.delete(account_obj)
        self.Session.commit()

    @logger_a
    def modify_password(self, new_password):
        account_obj = self.obj
        account_obj.user_password = md5_msg(new_password)
        obj_password = models.PasswordCase(password=new_password)
        find_obj = self.Session.query(models.PasswordCase).filter_by(
            password=new_password).first()
        # 避免创建重复的内容
        if not find_obj:
            self.Session.add(obj_password)
        self.Session.commit()

    def view_password(self):
        password_obj_list = self.Session.query(models.PasswordCase).all()
        password_list = [(i.id, md5_msg(i.password)) for i in password_obj_list]
        for password_tuple in password_list:
            if password_tuple[1] == self.obj.user_password:
                password_obj = self.Session.query(models.PasswordCase).filter_by(id=password_tuple[0]).first()
                return password_obj.password

    def view_simple_msg(self):
        # 返回简单的信息
        account_obj = self.obj
        user_id = account_obj.id
        user_type = account_obj.user_type
        user_name = account_obj.user_name
        return user_id, user_type, user_name

    @auth_password(name=ADMINISTRATOR)
    def view_detail_msg(self):
        user_id, user_type, user_name = self.view_simple_msg()
        user_password = self.view_password()
        return user_id, user_type, user_name, user_password


if __name__ == '__main__':
    # Session = models.create_session()
    # tmp = AdminModels(obj=Session.query(models.AccountMsg).filter(models.AccountMsg.id == 30).first(), session=Session)
    # print(tmp.obj.id)
    # tmp.modify_password(new_password='abcdegaa')
    # print('ok')
    # print(md5_msg('abcdegaa'))
    # tmp.view_password()
    # print('----')

    # msg = tmp.view_detail_msg()
    # print(msg)
    # tmp.delete_msg()
    # print('ok')
    pass