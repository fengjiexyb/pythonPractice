# -*- coding: utf-8 -*-  
"""
@created time:2018/7/19 10:08
@Python version: python 3.6.6(anaconda3  64-bit)
@contact:QQ:120405752,xuyongbingwork@126.com
@author: fengjiexyb
@license: Apache Licence 
@site: http://blog.csdn.net/fengjiexyb , https://github.com/fengjiexyb
@software: PyCharm Community Edition
@file: py_get_datatype_test.py
@description:
    python 及 numpy、 pandas 中存在多种获取数据类型的方法或属性，本程序用于分析多种方式的异同结果。
    本程序测试方法/属性有：
        type() ： python自带。用于获取变量的类型；
        dtype ： numpy 和pandas 共有属性（d表示data）。用于获取复合类型变量内部元素的类型；
        ftype ： pandas 属性。用于检查复合类型变量内部元素是稀疏还是稠密，只支持Series(内部元素同一类型的变量)。
        dtypes ：  pandas 属性。用于检查复合类型变量内部元素的类型。支持DataFrame(内部元素不属于同于类型) 和 Series(内部元素同一类型的变量)。
        ftypes ： pandas 属性。用于检查复合类型变量内部元素是稀疏还是稠密。支持DataFrame(内部元素不属于同于类型) 和 Series(内部元素同一类型的变量)。对于Series 和 ftype结果一样。
        get_dtype_counts() :  pandas 属性。用于统计复合类型变量内部元素的类型，每种类型有出现次数。支持DataFrame(内部元素不属于同于类型) 和 Series(内部元素同一类型的变量)。
        get_ftype_counts() :  pandas 属性。官方不建议使用。用于统计复合类型变量内部元素的是稀疏还是稠密，每种类型有出现次数。
                                支持DataFrame(内部元素不属于同于类型) 和 Series(内部元素同一类型的变量)。
    测试支持情况列表：
        数据类型         type()     dtype   ftype   dtypes()    ftypes()    get_dtype_counts()  get_ftype_counts()
        int                 Y       N       N       N           N           N                   N
        list                Y       N       N       N           N           N                   N
        ndarray             Y       Y       N       N           N           N                   N
        datetimeIndex       Y       Y       N       N           N           N                   N
        Series              Y       Y       Y       Y           Y           Y                   Y
        DataFrame           Y       Y       Y       Y           Y           Y                   Y
    详细结果在程序最下方。
"""
import re

import numpy as np
import pandas as pd

# 测试数据
TEST_DATA = {
    'int_testdata': 1,  # python 基本数据类型
    'list_testdata': [1, 3, 4],  # python 复合数据类型
    'ndarray_testdata': np.array([1, 3, 4]),  # numpy 数据类型
    'dti_testdata': pd.date_range('20130101', periods=6),  # pandas 数据类型 datetimeIndex
    'series_testdata': pd.Series([1, 3, 5, np.nan, 6, 8]),  # pandas 数据类型
    'df_testdata': pd.DataFrame({
                                    'A': 1.,
                                    'B': pd.date_range('20130101', periods=4),
                                    'C': pd.Series(1, index=list(range(4)), dtype="int32"),
                                    # 上一行提示："Expected type 'Optional[dtype]', got 'Type[dtype]' instead"
                                    # 这个问题可能是pycharm 的问题，pycharm对pandas和numpy 支持不是很完美。
                                    # 参考：https://stackoverflow.com/questions/30599676/expected-type-unionndarray-iterable-warning-in-python-instruction
                                    # 和 https://stackoverflow.com/questions/34318862/pycharm-type-hinting-weirdness
                                    'D': np.array([3] * 4, dtype='int32'),
                                    'E': pd.Categorical(["test", "train", "test", "train"]),
                                    'F': 'foo'})
    # pandas 数据类型 dataframe
}
# 测试的方法或属性名
TEST_FUN = ['type', 'dtype', 'ftype', 'dtypes', 'ftypes', 'get_dtype_counts', 'get_ftype_counts']


def main():
    for i, testdata in enumerate(TEST_DATA.values()):
        output_data_type(i, testdata)


def get_data_type(testdata, fun_type):
    """
    测试数据的方法或者属性的结果。
    :param testdata:待测试数据
    :param fun_type:待测试方法或属性的名字
    :return:测试是否成功，结果
    """
    try:
        if fun_type == 'type':
            return True, str(type(testdata))
        elif fun_type == 'dtype':
            return True, testdata.dtype
        elif fun_type == 'ftype':
            return True, testdata.ftype
        elif fun_type == 'dtypes':
            return True, testdata.dtypes
        elif fun_type == 'ftypes':
            return True, testdata.ftypes
        elif fun_type == 'get_dtype_counts':
            return True, str(testdata.get_dtype_counts())
        elif fun_type == 'get_ftype_counts':
            return True, str(testdata.get_ftype_counts())
        else:
            return False, None
    except BaseException as args:
        return False, args


def output_data_type(data_id, testdata):
    """
    输出type()、dtype、ftype、dtypes对于不同数据的结果。
    :param data_id: 测试数据（TEST_DATA）id
    :param testdata: 待测试的数据
    :return:null
    """
    match_obj = re.search(r'<class \'(.*?)\'>', str(type(testdata)), re.M | re.I)
    s_datatype = match_obj.group(1)
    data_id += 1
    print("----------------------", data_id, s_datatype, "----------------------")

    print(data_id, "0--- value:\n", testdata)
    for fun_id, fun_type in enumerate(TEST_FUN):
        res_flag, res = get_data_type(testdata, fun_type)
        if res_flag:
            print(data_id, fun_id + 1, "--- ", fun_type, ":", res)
        else:
            print(data_id, fun_id + 1, "---", s_datatype, "没有", fun_type, "方法/属性.", res)


if __name__ == '__main__':
    main()

"""
---------------------- 1 int ----------------------
1 0--- value:
 1
1 1 ---  type : <class 'int'>
1 2 --- int 没有 dtype 方法/属性. 'int' object has no attribute 'dtype'
1 3 --- int 没有 ftype 方法/属性. 'int' object has no attribute 'ftype'
1 4 --- int 没有 dtypes 方法/属性. 'int' object has no attribute 'dtypes'
1 5 --- int 没有 ftypes 方法/属性. 'int' object has no attribute 'ftypes'
1 6 --- int 没有 get_dtype_counts 方法/属性. 'int' object has no attribute 'get_dtype_counts'
1 7 --- int 没有 get_ftype_counts 方法/属性. 'int' object has no attribute 'get_ftype_counts'
---------------------- 2 list ----------------------
2 0--- value:
 [1, 3, 4]
2 1 ---  type : <class 'list'>
2 2 --- list 没有 dtype 方法/属性. 'list' object has no attribute 'dtype'
2 3 --- list 没有 ftype 方法/属性. 'list' object has no attribute 'ftype'
2 4 --- list 没有 dtypes 方法/属性. 'list' object has no attribute 'dtypes'
2 5 --- list 没有 ftypes 方法/属性. 'list' object has no attribute 'ftypes'
2 6 --- list 没有 get_dtype_counts 方法/属性. 'list' object has no attribute 'get_dtype_counts'
2 7 --- list 没有 get_ftype_counts 方法/属性. 'list' object has no attribute 'get_ftype_counts'
---------------------- 3 numpy.ndarray ----------------------
3 0--- value:
 [1 3 4]
3 1 ---  type : <class 'numpy.ndarray'>
3 2 ---  dtype : int32
3 3 --- numpy.ndarray 没有 ftype 方法/属性. 'numpy.ndarray' object has no attribute 'ftype'
3 4 --- numpy.ndarray 没有 dtypes 方法/属性. 'numpy.ndarray' object has no attribute 'dtypes'
3 5 --- numpy.ndarray 没有 ftypes 方法/属性. 'numpy.ndarray' object has no attribute 'ftypes'
3 6 --- numpy.ndarray 没有 get_dtype_counts 方法/属性. 'numpy.ndarray' object has no attribute 'get_dtype_counts'
3 7 --- numpy.ndarray 没有 get_ftype_counts 方法/属性. 'numpy.ndarray' object has no attribute 'get_ftype_counts'
---------------------- 4 pandas.core.indexes.datetimes.DatetimeIndex ----------------------
4 0--- value:
 DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
4 1 ---  type : <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
4 2 ---  dtype : datetime64[ns]
4 3 --- pandas.core.indexes.datetimes.DatetimeIndex 没有 ftype 方法/属性. 'DatetimeIndex' object has no attribute 'ftype'
4 4 --- pandas.core.indexes.datetimes.DatetimeIndex 没有 dtypes 方法/属性. 'DatetimeIndex' object has no attribute 'dtypes'
4 5 --- pandas.core.indexes.datetimes.DatetimeIndex 没有 ftypes 方法/属性. 'DatetimeIndex' object has no attribute 'ftypes'
4 6 --- pandas.core.indexes.datetimes.DatetimeIndex 没有 get_dtype_counts 方法/属性. 'DatetimeIndex' object has no attribute 'get_dtype_counts'
4 7 --- pandas.core.indexes.datetimes.DatetimeIndex 没有 get_ftype_counts 方法/属性. 'DatetimeIndex' object has no attribute 'get_ftype_counts'
---------------------- 5 pandas.core.series.Series ----------------------
5 0--- value:
 0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
5 1 ---  type : <class 'pandas.core.series.Series'>
5 2 ---  dtype : float64
5 3 ---  ftype : float64:dense
5 4 ---  dtypes : float64
5 5 ---  ftypes : float64:dense
5 6 ---  get_dtype_counts : float64    1
dtype: int64
5 7 ---  get_ftype_counts : float64:dense    1
dtype: int64
---------------------- 6 pandas.core.frame.DataFrame ----------------------
6 0--- value:
      A          B  C  D      E    F
0  1.0 2013-01-01  1  3   test  foo
1  1.0 2013-01-02  1  3  train  foo
2  1.0 2013-01-03  1  3   test  foo
3  1.0 2013-01-04  1  3  train  foo
6 1 ---  type : <class 'pandas.core.frame.DataFrame'>
6 2 --- pandas.core.frame.DataFrame 没有 dtype 方法/属性. 'DataFrame' object has no attribute 'dtype'
6 3 --- pandas.core.frame.DataFrame 没有 ftype 方法/属性. 'DataFrame' object has no attribute 'ftype'
6 4 ---  dtypes : A           float64
B    datetime64[ns]
C             int32
D             int32
E          category
F            object
dtype: object
6 5 ---  ftypes : A           float64:dense
B    datetime64[ns]:dense
C             int32:dense
D             int32:dense
E          category:dense
F            object:dense
dtype: object
6 6 ---  get_dtype_counts : float64           1
int32             2
datetime64[ns]    1
object            1
category          1
dtype: int64
6 7 ---  get_ftype_counts : float64:dense           1
int32:dense             2
datetime64[ns]:dense    1
object:dense            1
category:dense          1
dtype: int64
"""