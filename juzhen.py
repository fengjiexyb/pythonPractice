# -*- coding: utf-8 -*-  
"""
@finish time:2017/10/10 10:16
@Python version: python 2.7.13(anaconda2 4.4.0 64-bit)
@contact:QQ:120405752,xuyongbingwork@126.com
@author: fengjiexyb
@license: Apache Licence 
@site: http://blog.csdn.net/fengjiexyb , https://github.com/fengjiexyb
@software: PyCharm Community Edition
@file: juzhen.py
@content: array multiply used numpy
"""
import numpy as np


def numpy_multiply():
    a = np.array([0.2, 0.3, 0.5])
    print a
    b = np.array([[0.7, 0.2, 0.1], [0.1, 0.2, 0.7], [0.3, 0.6, 0.1]])
    print b
    # element-wise product
    print np.multiply(a, b)
    print a * b
    # multiply in linear algebra
    print np.dot(a, b)


def main():
    numpy_multiply()


if __name__ == '__main__':
    main()
