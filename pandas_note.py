# -*- coding: utf-8 -*-  
"""
@created time:2018/7/13 14:56
@Python version: python 2.7.13(anaconda2 4.4.0 64-bit)
@contact:QQ:120405752,xuyongbingwork@126.com
@author: fengjiexyb
@license: Apache Licence 
@site: http://blog.csdn.net/fengjiexyb , https://github.com/fengjiexyb
@software: PyCharm Community Edition
@file: pandas_note.py
@description:
    pandas 官方基础教程笔记（有修改）
    http://pandas.pydata.org/pandas-docs/stable/10min.html
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

N = 6  # 创建对象时的行数。


def create_object():
    """
    创建对象。主要包括Series、DataFrame、datetimeIndex。
    merge_data()中的join方法部分有一种生成DataFrame方法。
    :return:返回Series、DataFrame、datetimeIndex。供后续使用。
    """
    print('======创建对象======')
    print('------创建series序列------')
    # 创建Series有多种方式，参考：https://blog.csdn.net/brucewong0516/article/details/79196902
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    # 运行程序出现AttributeError: module 'pandas' has no attribute 'Series'错误.
    # 解决方式：文件名不可以是pandas。参考https://stackoverflow.com/questions/30227883/object-pandas-has-no-attribute-name-series。
    # （网上答案：在Anaconda Prompt上运行：conda update --all .更新包）
    print(s)
    print('------创建DateFrame------')

    dates = pd.date_range('2018-01-01', periods=N)  # 从2018-01-01开始30天的日期
    print(dates)
    print('------创建DateFrame,以时间为行名，list为列名，随机数为值------')
    df = pd.DataFrame(np.random.randn(N, 4), index=dates, columns=list('ABCD'))
    print(df)

    df2 = pd.DataFrame({
                        'A': 1.,
                        'B': pd.Timestamp('2018-01-01'),
                        'C': pd.Series(1, index=list(range(4)), dtype="int32"),
                        # 上一行提示："Expected type 'Optional[dtype]', got 'Type[dtype]' instead"
                        # 这个问题可能是pycharm 的问题，pycharm对pandas和numpy 支持不是很完美。
                        # 参考：https://stackoverflow.com/questions/30599676/expected-type-unionndarray-iterable-warning-in-python-instruction
                        # 和 https://stackoverflow.com/questions/34318862/pycharm-type-hinting-weirdness
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
    print(df2)
    return s, df, dates


def view_data(df):
    """
    查看DataFrame数据。
    :param df: DataFrame
    :return:
    """
    print("======查看对象======")
    print("------查看前5条数据-----")
    print(df.head())  # 默认5条
    print("------查看最后3条数据-----")
    print(df.tail(3))
    print("------查看数据索引(行名)-----")
    print(df.index)
    print("------查看数据列名-----")
    print(df.columns)
    print("------查看数据值(不显示行列名)-----")
    print(df.values)
    print("------基本统计值(按列,包括：计数、平均值、标准差、最小值、四分位数（3个）、最大值)-----")
    print(df.describe())
    print("------转置-----")
    print(df.T)
    print("------按索引（行名或列名）排序-----")
    print(df.sort_index(axis=0, ascending=False))  # ascending=True 表示升序排列。axis=0表示按行名排序，axis=1表示按列名排序
    print("------按某一行（列）的值排序-----")
    # 原型：def sort_values(self, by, axis=0, ascending=True, inplace=False,kind='quicksort', na_position='last'):
    print(df.sort_values(by='B'))


def selection_data(df, dates):
    """
        选择DataFrame数据。
        在方法最后出现：复制DataFrame，给DataFrame添加新列
        :param df: DataFrame
        :param dates: DataFrame列名时间序列
        :return:None
        """
    print("======选择数据======")
    print("------选择某列（列名）数据，返回Series-----")
    print(df['A'])  # 也可以写作df.A
    # print(df['20180101'])  # 注意这种方法是错误的。
    print("------选择某列（列名）数据-----")
    print(df.loc[dates[0]])
    print("------选择某行（id）数据-----")
    print(df[0:3])
    print(df['20180101':'20180103'])
    print("------通过索引选择数据(4种)-----")
    # print(df[:, ['A', 'B']])  # 注意：此方法在官方文档可以，实测不能运算。
    print(df.loc['20180102':'20180104', ['A', 'B']])
    print('\n')
    print(df.loc['20180102', ['A', 'B']])
    print('\n')
    print(df.loc[dates[0], 'A'])
    print('\n')
    print(df.at[dates[0], 'A'])
    # loc可以让你按照索引来进行行列选择。
    # at的使用方法与loc类似，但是比loc有更快的访问数据的速度，而且只能访问单个元素，不能访问多个元素。
    print("------通过位置选择数据-----")
    print(df.iloc[3])
    print('\n')
    print(df.iloc[3:5, 0:2])
    print('\n')
    print(df.iloc[[1, 2, 4], [0, 2]])
    print('\n')
    print(df.iloc[1:3, :])
    print('\n')
    print(df.iloc[1, 1])
    print('\n')
    print(df.iat[1, 1])
    print("------通过布尔判断选择数据-----")
    print(df[df.A > 0])  # 选取A列大于0的行
    print('\n')
    print(df[df > 0])  # 选取大于0的值，保持原格式。
    print('\n')
    print("------通过isin()判断选择数据-----")
    # 复制DataFrame，给DataFrame添加一列
    df2 = df.copy()
    df2['E'] = ['one', 'two', 'three', 'four', 'five', 'six']  # 这里不能用df.F。df.F只能是引用。
    print(df)
    print(df2[df2.E.isin(['two', 'four'])])  # 选取A列大于0的行。df.E可以写作df['E']
    print('\n')


def assign(df, dates):
    """
    赋值运算。compute_missingvalue中也存在赋值操作。
    :param df: DataFrame
    :param dates: DataFrame列名时间序列
    :return:
    """
    print("======赋值操作======")
    print("------新建Series------")
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('2018-01-01', periods=6))
    print(s1)
    print("------把Series赋值给DataFrame作为一列（可以使新列）------")
    df['F'] = s1  # 这里不能用df.F。df.F只能是引用。
    df.A = s1
    print("------通过标签/位置赋值------")
    df.at[dates[0], 'B'] = 0
    df.iat[0, 3] = 0
    df.loc[:, 'C'] = np.array([5] * len(df))
    print(df)
    print("------通过布尔判断赋值------")
    df2 = df.copy()
    df2[df2 > 0] = -df2  # 全部元素取反
    print(df2)


def compute_missingvalue(df, dates):
    """
        缺失值处理。pandas 主要用np.nan表示缺失数据，默认不列入计算。
        :param df: DataFrame
        :param dates: DataFrame列名时间序列
        :return:
    """
    print("=====缺失值处理=====")
    print('-----添加一列-----')
    df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])  # 添加空列
    df1.loc[dates[0]:dates[1], 'E'] = 1  # 赋值
    print(df1)
    print('-----删除存在缺失值的列-----')
    df2 = df1.dropna(how='any')
    print(df2)
    print('-----填充缺失值-----')
    df2 = df1.fillna(value=5)
    print(df2)
    print('-----判断是否缺失，返回布尔集-----')
    df2 = pd.isnull(df1)  # 其他操作：notna()\notnull\isna
    print(df2)


def operation_data(df, dates):
    """
    基本数据操作。
    :param df: DataFrame
    :param dates: DataFrame列名时间序列
    :return:
    """
    print("======数据操作======")
    print('------计算平均数------')
    print(df.mean())  # 默认值为0（按列计算），如果填写1，则按行运算。
    print('------数据相减------')
    s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)  # shift 表示向后推移2个格子。
    print(df)
    print(df.sub(s, axis='index'))  # df 和s相减，注意：由于s存在Nan，所以和Nan相减的结果还是Nan。参考compute_missingvalue()方法注释。
    # axis取值范围 {0, 1, ‘index’, ‘columns’}
    # Series 也有 sub 函数
    print('------函数操作数据------')
    print(df.apply(lambda x: x.max() - x.min()))
    # 原型：DataFrame.apply(func, axis=0, broadcast=None, raw=False, reduce=None, result_type=None, args=(), **kwds)
    # axis可以选择按行操作或者按列操作 默认按列（从上到下）
    print(df.apply(np.cumsum))  # cumsum：累加操作
    print('------统计元素出现次数------')
    s = pd.Series(np.random.randint(0, 7, size=10))
    print(s)
    print(s.value_counts())  # 默认按出现次数从大到小排序。
    print('------字符串操作------')
    s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
    print(s.str.lower())  # 其他Python的字符串操作都可以使用。


def merge_data():
    """
    合并数据。
    :return:
    """
    print("======合并数据======")
    print('------concat方法------')
    df = pd.DataFrame(np.random.randn(10, 4))
    pieces = [df[:3], df[3:7], df[7:]]
    print(pd.concat(pieces))
    print('------join方法(可以用该方法生成笛卡尔积)------')
    left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
    right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
    print(pd.merge(left, right, on='key'))
    print('------append方法------')
    df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
    s = df.iloc[3]  # 第4行
    print(df)
    print(df.append(s, ignore_index=False))  # 把第4行追加到df中。ignore_index如果为False，使用原来的行名；默认为False。


def group_data():
    """
    分组数据。
    :return:
    """
    print("======分组数据======")
    df = pd.DataFrame({
                        'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                        'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                        'C': np.random.randn(8),
                        'D': np.random.randn(8)
                        })
    print(df)
    print('------分组求和------')
    print(df.groupby('A').sum())
    print(df.groupby(['A', 'B']).sum())


def reshape():
    """
    变形
    :return:
    """
    print("======变形======")
    tuples = list(zip(*[
                        ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                        ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
    index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
    df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
    print(df)
    print("------stack方法------")
    stacked = df.stack()
    print(stacked)
    print(stacked.unstack(1))  # 默认值是最后一层，在示例中应该是2


def pivot_table():
    """
    透视表
    :return:
    """
    print("======透视表======")
    df = pd.DataFrame({
                        'A': ['one', 'one', 'two', 'three'] * 3,
                        'B': ['A', 'B', 'C'] * 4,
                        'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                        'D': np.random.randn(12),
                        'E': np.random.randn(12)})
    print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))


def process_time_series():
    """
    时间序列处理
    :return:
    """
    print("======时间序列处理======")
    print("------时间分组处理------")
    rng = pd.date_range('1/1/2012', periods=100, freq='S')  # 生成时间序列，100个元素，日期是2012-01-01，间隔是1秒。
    ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)  # 以时间序列为行名，生成随机数序列。
    print(ts.resample('5Min').sum())  # 求和.每隔5Min一组。
    print("------时间样式处理------")
    rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
    ts = pd.Series(np.random.randn(len(rng)), rng)
    print(ts)
    ts_utc = ts.tz_localize('UTC')  # 调整时间样式
    print(ts_utc)
    print("------调整时区------")
    print(ts_utc.tz_convert('US/Eastern'))
    print("------调整时间跨度------")
    ts = ts.to_period('M')  # 时间跨度是月
    print(ts)
    ts = ts.to_timestamp()  # 时间跨度调整回原始状态，只是跨度，具体的数值已经找不到了。
    print(ts)
    print("------调整时间跨度2------")
    prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
    # freq的取值范围参考：http://pandas.pydata.org/pandas-docs/stable/timeseries.html 中的 Offset Aliases 和 Anchored Offsets 部分。
    # pandas真他妈坑，
    # Q 表示 按季度。NOV 表示设置十一月份是一年的最后一个月，所以下面才会出现+1的情况（prng.asfreq('M', 'e') + 1)）
    print(prng)
    ts = pd.Series(np.random.randn(len(prng)), prng)
    ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
    # asfreq 变换跨度。M表示跨度变为月份。e表示显示季度的最后一个月（默认值是e，end）
    # 同理 asfreq('H', 's') 表示跨度变为小时，显示每个月的第一个小时
    print(ts.head())


def categoricals():
    """
    Categoricals 类别？
    :return:
    """
    print("======Categoricals======")
    print("------原始值------")
    df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
    print(df)
    print("------转换category类型------")
    df["grade"] = df["raw_grade"].astype("category")
    # astype 转换类型
    print(df["grade"])  # 结果中包含：Categories (3, object): [a, b, e]
    print("------给category列重新赋值------")
    df["grade"].cat.categories = ["very good", "good", "very bad"]  # 给grade重新赋值。
    print(df["grade"])
    print(df)
    print("------添加类别，但不赋值------")
    df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
    print("------排序------")
    df.sort_values(by="grade")  # 排序
    print(df)
    print("------统计------")
    print(df.groupby("grade").size())  # 统计


def plotting():
    """
       画图
       :return:
       """
    print("======画图======")
    print("------一条折线图------")
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    plt.show()
    print("------多条折线图------")
    # 多条折线图参考：https://blog.csdn.net/hustqb/article/details/54410670
    # 官方文档的代码没有通过。
    df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), columns=list('ABCD'), index=np.arange(0, 100, 10))
    df.plot()
    plt.show()


def read_and_write_csv(df):
    """
    csv文件输入输出获取数据
    :return:
    """
    print("======csv文件======")
    df.to_csv('foo.csv')
    pd.read_csv('foo.csv')


def read_and_write_hdf5(df):
    """
    HDF5文件输入输出获取数据
    :return:
    """
    print("======hdf5文件======")
    df.to_hdf('foo.h5', 'df')
    pd.read_hdf('foo.h5', 'df')


def read_and_write_excel(df):
    """
    Excel 文件输入输出获取数据
    :return:
    """
    print("======Excel文件======")
    df.to_excel('foo.xlsx', sheet_name='Sheet1')
    pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])


def main():
    s, df, dates = create_object()
    view_data(df)
    selection_data(df, dates)
    assign(df, dates)
    compute_missingvalue(df, dates)
    operation_data(df, dates)
    merge_data()
    group_data()
    reshape()
    pivot_table()
    process_time_series()
    categoricals()
    plotting()
    read_and_write_csv(df)
    read_and_write_hdf5(df)
    read_and_write_excel(df)


if __name__ == '__main__':
    main()
