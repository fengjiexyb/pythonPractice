# -*- coding: utf-8 -*-  
"""
@finish time:2017/10/16 18:25
@Python version: python 2.7.13(anaconda2 4.4.0 64-bit)
@contact:QQ:120405752,xuyongbingwork@126.com
@author: fengjiexyb
@license: Apache Licence 
@site: http://blog.csdn.net/fengjiexyb , https://github.com/fengjiexyb
@software: PyCharm Community Edition
@file: fun.py
@content:function exercise
"""


def fun():
    """ this is a word. """
    fun.__doc__ = "dddd"
    fun.version = "v0.2"
    print fun.__doc__
    print fun.version
    pass


def main():
    fun()
    # print fun.__doc__
    fun.version = 0.1
    print fun.version


if __name__ == '__main__':
    main()
