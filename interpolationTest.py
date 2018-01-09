# -*- coding: utf-8 -*-  
"""
@created time:2018/1/2 15:14
@Python version: python 2.7.13(anaconda2 4.4.0 64-bit)
@contact:QQ:120405752,xuyongbingwork@126.com
@author: fengjiexyb
@license: Apache Licence
@site: http://blog.csdn.net/fengjiexyb , https://github.com/fengjiexyb
@software: PyCharm Community Edition
@file: interpolationTest.py
@content: 登革热系统的天气数据从气象中心（2017年之前）和环境云平台（2017年及以后）上获取。但是获取的数据存在许多缺失值。
            为了补全这些缺失值，本程序测试了多种插值方法，并利用折线图显示。
"""
import cx_Oracle
import pylab as pl
from scipy.interpolate import UnivariateSpline
import numpy as np
import random
from scipy.interpolate import interp1d
from random import choice


connect = 'hii/hii@200.100.100.193/dgr'
conn = cx_Oracle.connect(connect)
cur = conn.cursor()
color_sequence = ['white', 'blue', 'cyan', 'green', 'black', 'magenta', 'red', 'yellow']  # 图片颜色列表，第一个白色不使用
image_index = 1  # 表示第几幅图（一共7张）


def get_weather_data():
    """
        获取数据，测试数据只使用了FTEMPERATURE_MEAN字段。
    """
    sql = ("select "
           " fsiteid, "
           " to_char(frecorddate, 'yyyy-mm-dd'),"
           " FTEMPERATURE_MEAN, "
           " FTEMPERATURE_MAX, "
           " FTEMPERATURE_MIN, "
           " frainfall, "
           " fhumidity "
           "from imp_weather_data "
           "where fsiteid = '101280210' "
           "and fyear='2017' "
           "order by FRECORDDATE")
    wea_data = cur.execute(sql)
    wea_data = wea_data.fetchall()
    return wea_data


def main():
    wea_dataset = get_weather_data()  # 获取数据
    xInt = []  # 原始数据x轴
    yInt = []  # 原始数据y轴
    index = 0
    """
    如果不使用if判断，就会把空值也放进原始数据中，这样在填充的时候就会忽略这些空值（认为这是正确的值）。
    但是index不能省略（即使y是空值，x也要有值）如果省略了，填充的时候就找不到空值的位置了。
    """
    for wea_data in wea_dataset:
        index = index + 1
        if wea_data[2] is None:
            pass
        else:
            xInt.append(index)
            yInt.append(wea_data[2])

    sub_plot(xInt, yInt, "Linear")  # 原始图
    """
    linspace生成一个数字序列，参数分别为：开始值、截止值、序列数字个数
    """
    xnew = np.linspace(1, index, index)
    """
    UnivariateSpline 是适合于给定数据点集合的“一维平滑样条曲线”，可以对数据集边界的缺失值进行补值。
    参数s如果小于0 表示强制通过所有已存在的数据点.s越大，曲线越平滑
    """
    f = UnivariateSpline(xInt, yInt, s=9)
    ynew = f(xnew)
    sub_plot(xnew, ynew, "UnivariateSpline")
    """
    interp1d不能对数据集边界的缺失值进行补值。所以x轴从2开始（查询的第一条数据就是缺失值）
    """
    xnew = np.linspace(2, index, index)
    for kind in ["nearest", "zero", "slinear", "quadratic", "cubic"]:  # 插值方式
        """
        插值方式参考：https://www.jianshu.com/p/b306095309db
        """
        f = interp1d(xInt, yInt, kind=kind)
        ynew = f(xnew)
        sub_plot(xnew, ynew, str(kind))
    pl.show()
    """
    pandas中的interpolate（）也可以进行插值，但是未执行成功。
    可以参考https://jingyan.baidu.com/article/a501d80cf7c9c3ec620f5e5a.html
    """


def sub_plot(x, y, str_label):
    """
    画子图功能
    :param x: 数据横坐标值
    :param y: 数据纵坐标值
    :param str_label: 图例
    :return: null
    """
    global image_index  # 图表位置、线条颜色
    pl.subplot(4, 2, image_index)  # 4行2列，image_index表示位置
    pl.plot(x, y, color=color_sequence[image_index], label=str_label)
    image_index = image_index + 1


if __name__ == '__main__':
    main()
