#!/usr/bin/env python3
# coding=utf-8

"""
@File：models.py
@Author：seeker0720
@Date：2019/10/7 18:55
@Instructions:
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from conf.settings import ENGINE


engine = create_engine(f'{ENGINE}')
Base = declarative_base()


class LoginMsg(Base):
    __tablename__ = 'login_msg'
    id = Column(Integer, primary_key=True)
    login_name = Column(String(64), nullable=False, unique=True)
    login_password = Column(String(64), nullable=False)

    # def __repr__(self):
    #     return f'{self.id}'


class AccountMsg(Base):
    __tablename__ = 'account_msg'
    id = Column(Integer, primary_key=True)
    user_type = Column(String(64), nullable=False)
    user_name = Column(String(64), nullable=False)
    user_password = Column(String(64), nullable=False)
    login_user_id = Column(Integer, ForeignKey('login_msg.id'))

    login_msg = relationship('LoginMsg', backref='account_msg')

    def __repr__(self):
        return f'{self.user_type}'


class PasswordCase(Base):
    __tablename__ = 'password_data'
    id = Column(Integer, primary_key=True)
    password = Column(String(64), nullable=False)

    def __repr__(self):
        return f'{self.password}'


def create_session():
    """构造表结构，生成Session实例"""
    Base.metadata.create_all(engine)
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()
    return Session


if __name__ == '__main__':
    # Session = create_session()
    # obj = Session.query(AccountMsg).filter_by(user_type='test').first()
    # print(obj.login_msg.login_name)
    # obj.user_password = 'teesss'
    # Session.commit()
    # print('ok')
    pass