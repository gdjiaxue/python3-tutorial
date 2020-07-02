#/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def hello():
    """first function"""
    print('Hello World')
    print('current path', os.getcwd())


if __name__ == '__main__':
    hello()
