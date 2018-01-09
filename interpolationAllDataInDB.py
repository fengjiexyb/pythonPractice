# -*- coding: utf-8 -*-
"""
@created time:2018/1/3 9:22
@Python version: python 2.7.13(anaconda2 4.4.0 64-bit)
@contact:QQ:120405752,xuyongbingwork@126.com
@author: fengjiexyb
@license: Apache Licence
@site: http://blog.csdn.net/fengjiexyb , https://github.com/fengjiexyb
@software: PyCharm Community Edition
@file: interpolationAllDataInDB.py
@content:登革热系统的天气数据从气象中心（2017年之前）和环境云平台（2017年及以后）上获取。但是获取的数据存在许多缺失值。
            为了补全这些缺失值，本程序使用UnivariateSpline插值算法进行补值。
            UnivariateSpline算法的有点在于1、插值曲线平滑；2、可以外插值。
            具体对比结果参考interpolationTest.py
            由于数据量较大，程序先读取监测点（198个）；对每个监测点查出所有数据（最多4800+条）；对每组数据进行插值；
            判断存在空值的记录，更新数据库的相关行。
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


def get_weather_data(site_id):
    """
        获取天气数据。
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
           "where fsiteid = " + site_id +
           "order by FRECORDDATE")
    wea_data = cur.execute(sql)
    wea_data = wea_data.fetchall()
    return wea_data


def get_site_data():
    """
        获取数据，找到所有监测站点，分别处理。
    """
    sql = "select distinct fsiteid from imp_weather_data"
    wea_data = cur.execute(sql)
    wea_data = wea_data.fetchall()
    return wea_data


def main():
    all_site_id = get_site_data()  # 获取监测站数据
    for site_id in all_site_id:
        interpolation_weather_data = []
        # 获取天气数据，site_id表示数据库查询的一条记录（尽管该记录只有一个字段），site_id[0]表示监测站点编号
        original_weather_data = get_weather_data(site_id[0])
        print site_id
        for field_id in range(2, 7):  # 要处理的字段号
            interpolation_weather_data.append(interpolation(original_weather_data, field_id))
        # print len(interpolation_weather_data[1, 1])
        # 将list转为np.array
        arr_interpretation_weather_data = np.array(interpolation_weather_data)
        """ 这部分不需要，真实值是存在负值的
        # 将array中小于0的值都设为0.
        mask = arr_interpretation_weather_data < 0
        arr_interpretation_weather_data[mask] = 0
        """
        # 这个数据，行表示插值的字段（最高气温、最低气温、平均气温、湿度、降雨量）
        # 列表示日期，所以要计算列的长度。
        # 也可以将array转置（arr_interpretation_weather_data.T）再取一行
        print len(arr_interpretation_weather_data[1])
        for i in range(len(arr_interpretation_weather_data[1])):
            # 判断每个字段是否为空（最高气温、最低气温、平均气温、降雨量、湿度），只要有一个为空就更新。
            if original_weather_data[i][2] is None or original_weather_data[i][3] is None \
               or original_weather_data[i][4] is None or original_weather_data[i][5] is None\
               or original_weather_data[i][6] is None:
                update_weather_database(original_weather_data[i][0],
                                        original_weather_data[i][1],
                                        arr_interpretation_weather_data[:, i]  # 这种取一列的方式不适用于list,
                                        )


def update_weather_database(site_id, record_time, interpretation_data):
    """
    更新数据库数据
    :param site_id: 监测站点
    :param record_time: 记录日期（不含时间）
    :param interpretation_data: 插值后的数据（只有当前要更新的行）
    :return: null
    """
    sql = ("update imp_weather_data "
           "set FTEMPERATURE_MEAN = '%.1f', FTEMPERATURE_MAX = '%.1f', FTEMPERATURE_MIN = '%.1f',"
           " frainfall = '%.1f', fhumidity = '%d' where fsiteid = '%s'"
           " and to_char(frecorddate, 'yyyy-mm-dd')='%s'" %
           (interpretation_data[0],
            interpretation_data[1],
            interpretation_data[2],
            interpretation_data[3],
            interpretation_data[4],
            site_id,
            record_time))
    cur.execute(sql)
    # print sql
    conn.commit()


def interpolation_wea_data(original_weather_data, field_id):
    print field_id
    xInt = []  # 原始数据x轴
    yInt = []  # 原始数据y轴
    index = 0
    """
        如果不使用if判断，就会把空值也放进原始数据中，这样在填充的时候就会忽略这些空值（认为这是正确的值）。
        但是index不能省略（即使y是空值，x也要有值）如果省略了，填充的时候就找不到空值的位置了。
    """
    for wea_data in original_weather_data:
        index = index + 1
        if wea_data[field_id] is None:
            pass
        else:
            xInt.append(index)
            yInt.append(wea_data[field_id])

    # linspace 生成一个数字序列，参数分别为：开始值、截止值、序列数字个数
    xnew = np.linspace(1, index, index)

    # UnivariateSpline 是适合于给定数据点集合的“一维平滑样条曲线”，可以对数据集边界的缺失值进行补值。
    f = UnivariateSpline(xInt, yInt, s=9)
    ynew = f(xnew)
    return ynew


if __name__ == '__main__':
    main()
