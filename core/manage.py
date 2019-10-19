#!/usr/bin/env python3
# coding=utf-8

"""
@File：manage.py
@Author：seeker0720
@Date：2019/10/8 2:07
@Instructions:
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.get_command_line_argv import get_argv
from core import main

cmd = get_argv()

if cmd == 'createpassword':
    main.create_password()
elif cmd == 'runapp':
    main.run()
else:
    print('Sorry!!')
    pass


