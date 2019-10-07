#!/usr/bin/env python3
# coding=utf-8

"""
@File：get_command_line_argv.py
@Author：seeker0720
@Date：2019/10/8 1:27
@Instructions:
"""
import sys


def get_argv():
    try:
        command = sys.argv[1]
    except IndexError:
        pass
    else:
        return command
