# -*- coding: utf-8 -*-  
"""
@created time:2018/1/17 14:23
@Python version: python 2.7.13(anaconda2 4.4.0 64-bit)
@contact:QQ:120405752,xuyongbingwork@126.com
@author: fengjiexyb
@license: Apache Licence 
@site: http://blog.csdn.net/fengjiexyb , https://github.com/fengjiexyb
@software: PyCharm Community Edition
@file: compute.py
@content:没有什么特别功能，只是做一个计算而已。
"""


import numpy as np

w = np.array([[0.3, 0.5, 0.15, 0.15],
             [0.4, 0.3, 0.15, 0.15],
             [0.25, 0.25, 0.25, 0.25],
             [0.15, 0.15, 0.6, 0.1],
             [0.1, 0.2, 0.65, 0.05],
             [0.2, 0.4, 0.2, 0.2]])


def get_euclidean_metric(vector1, vector2 ):
    """
    :param vector1: 向量1
    :param vector2: 向量2
    :return: 两个向量的欧氏距离
    欧氏距离是两个向量的每一组值相减，计算结果的平方和再开方。相当于2级范数。
    """
    return sum([i * i for i in (vector1 - vector2)]) ** 0.5


def vector_normalization(i):
    """
    :param i:向量在矩阵中的行号
    :return:向量标准化结果
    向量的每一个元素减去向量元素平均值，对所有的差值计算平方和，再开方。
    本方法为了方便计算，先计算向量的均差，对均差乘以向量长度，在开方。
    均差计算公式：https://baike.baidu.com/item/%E6%96%B9%E5%B7%AE%E5%85%AC%E5%BC%8F/3638551?fr=aladdin
    """
    return (np.var(w[i]) * len(w[i])) ** 0.5


def sum_euclidean_metric(j):
    """
    计算第j个向量与其余所有向量的欧式距离之和
    :param j: 标准向量索引值
    :return: 欧式距离之和
    """
    em_sum = 0
    for i in range(6):
        em_sum += get_euclidean_metric(w[j], w[i])
    return em_sum


def main():
    for j in range(6):
        print 'a%d = %f' % (j, (0.5 * sum_euclidean_metric(j) + 0.5 * vector_normalization(j)))


if __name__ == '__main__':
    main()
