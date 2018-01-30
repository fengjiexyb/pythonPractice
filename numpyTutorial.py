# -*- coding: utf-8 -*-  
"""
@created time:2018/1/19 10:00
@Python version: python 2.7.13(anaconda2 4.4.0 64-bit)
@contact:QQ:120405752,xuyongbingwork@126.com
@author: fengjiexyb
@license: Apache Licence 
@site: http://blog.csdn.net/fengjiexyb , https://github.com/fengjiexyb
@software: PyCharm Community Edition
@file: numpyTutorial.py
@content:争取用一个代码来把大部分numpy的知识点串联起来。
        在阅读之前，你熟悉简单的python语法。
        未整理内容：numpy可以做简单的直方图，可以读取文件（np.save 、np.load）

        本文参考：http://blog.csdn.net/chen_shiqiang/article/details/51868115
                  https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
                  https://zhuanlan.zhihu.com/p/24309547（包含一些matplotlib）
                  http://blog.csdn.net/qq_34162294/article/details/53727357
                  https://www.jianshu.com/p/57e3c0a92f3a（包含一些matplotlib）
"""
import numpy as np
from numpy import pi
import chardet
import numpy.random as random
import sys

CREATE_ARRAY_TYPE = 1  # 创建数组类型，详见create_array()
"""
序号	数据类型及描述
1.	bool_ 存储为一个字节的布尔值（真或假）
2.	int_ 默认整数，相当于 C 的long，通常为int32或int64
3.	intc 相当于 C 的int，通常为int32或int64
4.	intp 用于索引的整数，相当于 C 的size_t，通常为int32或int64
5.	int8 字节（-128 ~ 127）
6.	int16 16 位整数（-32768 ~ 32767）
7.	int32 32 位整数（-2147483648 ~ 2147483647）
8.	int64 64 位整数（-9223372036854775808 ~ 9223372036854775807）
9.	uint8 8 位无符号整数（0 ~ 255）
10.	uint16 16 位无符号整数（0 ~ 65535）
11.	uint32 32 位无符号整数（0 ~ 4294967295）
12.	uint64 64 位无符号整数（0 ~ 18446744073709551615）
13.	float_ float64的简写
14.	float16 半精度浮点：符号位，5 位指数，10 位尾数
15.	float32 单精度浮点：符号位，8 位指数，23 位尾数
16.	float64 双精度浮点：符号位，11 位指数，52 位尾数
17.	complex_ complex128的简写
18.	complex64 复数，由两个 32 位浮点表示（实部和虚部）
19.	complex128 复数，由两个 64 位浮点表示（实部和虚部）
"""


def array_attribute(a):
    """
    查看数组属性。
    :param a: 数组
    :return:
    """
    """
    NumPy的主要对象是同种元素的多维数组。这是一个所有的元素都是一种类型、通过一个正整数元组索引的元素表格(通常是元素是数字)。
    在NumPy中维度(dimensions)叫做轴(axes)，轴的个数叫做秩(rank)。
    NumPy的数组类被称作 ndarray 。通常被称作数组。注意numpy.ndarray和标准Python库类array.array并不相同，
    后者只处理一维数组和提供少量功能。更多重要ndarray对象属性有：
    ndarray.ndim:数组轴的个数，在python的世界中，轴的个数被称作秩
    ndarray.shape:数组的维度。这是一个指示数组在每个维度上大小的整数元组。
                例如一个n排m列的矩阵，它的shape属性将是(2,3),这个元组的长度显然是秩，即维度或者ndim属性
    ndarray.size:数组元素的总个数，等于shape属性中元组元素的乘积。
    ndarray.dtype:一个用来描述数组中元素类型的对象，可以通过创造或指定dtype使用标准Python类型。另外NumPy提供它自己的数据类型。
    ndarray.itemsize:数组中每个元素的字节大小。
                    例如，一个元素类型为float64的数组itemsiz属性值为8(=64/8),又如，一个元素类型为complex32的数组item属性为4(=32/8).
    ndarray.data:包含实际数组元素的缓冲区，通常我们不需要使用这个属性，因为我们总是通过索引来使用数组中的元素。
    """
    print '-------------数组属性-----------------'
    print '数组a ='
    array_print(a, True)
    print 'a的维度 ='
    print a.shape
    print "a的秩 ="
    print a.ndim
    print "a元素类型 ="
    print a.dtype.name
    print "a元素大小（字节） ="
    print a.itemsize
    print "a元素个数 ="
    print a.size
    print "a的类型 ="
    print type(a)
    print '数组属性（详见注释）：'
    print a.flags
    """
    ndarray对象拥有以下属性。这个函数返回了它们的当前值。(flags应该是属性吧，不应该是方法)
    序号	属性及描述
    1.	C_CONTIGUOUS (C) 数组位于单一的、C 风格的连续区段内
    2.	F_CONTIGUOUS (F) 数组位于单一的、Fortran 风格的连续区段内
    3.	OWNDATA (O) 数组的内存从其它对象处借用
    4.	WRITEABLE (W) 数据区域可写入。 将它设置为flase会锁定数据，使其只读
    5.	ALIGNED (A) 数据和任何元素会为硬件适当对齐
    6.	UPDATEIFCOPY (U) 这个数组是另一数组的副本。当这个数组释放时，源数组会由这个数组中的元素更新

    """
    print '-------------数组属性结束-----------------'
    """结果展示
    a =
    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]]
    a的维度 =
    (3L, 5L)
    a的秩 =
    2
    a元素类型 =
    int32
    a元素大小（字节） =
    4
    a元素个数 =
    15
    a的类型 =
    <type 'numpy.ndarray'>
    数组属性（详见注释）：
      C_CONTIGUOUS : True
      F_CONTIGUOUS : True
      OWNDATA : True
      WRITEABLE : True
      ALIGNED : True
      UPDATEIFCOPY : False
    """


def create_array(create_type):
    """    常用的创建数组方式。
    :param create_type: 创建类型.由于类型多，所以使用了整数。
    :return: 创建的数组。
    """
    return {
        0: np.arange(6),  # 相当于python中的range
        1: np.arange(4).reshape(2, 2),
        2: np.array([[1, 2], [3, 4]], dtype=complex),  # 指定元素类型,其他数据类型在上面有。
        3: np.zeros((3, 4)),  # 3*4大小全0数组
        4: np.ones((2, 3, 4), dtype=np.int16),
        5: np.arange(0, 2, 0.3),  # 0-2,步长为0.3.  ([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])
        6: np.eye(10, k=-1, dtype=int),  # 生成对角线为1，其余元素为0的数组。k表示1的斜线在主对角线的偏移（测试下看看），可省略。
        7: np.identity(3),  # 单位矩阵。
        8: np.random.rand(3, 2),  # 生成3*2 大小的随机矩阵。元素在[0,1)之间
        9: 2.5 * np.random.randn(2, 4) + 3,  # 生成2*4 大小的随机矩阵，元素具有标准正态分布
        10: np.random.random(size=(2, 2)),  # 生成随机浮点数数组
        11: np.random.choice(5, 3, replace=False),  # 生成1*3大小矩阵，元素在0-5之间选择整数。5相当于一个np.arange(5)。replace=False选择元素不重复
        12: np.random.choice(5, size=(3, 2)),  # 生成2*3大小矩阵，元素在0-5之间选择整数。
        13: np.linspace(0, 2 * pi, 100),  # 0-2pi之间选取100个元素
        14: np.empty([2, 2], dtype=int),  # 空数组
        15: create_zero_array(),  # 全0数组
        16: create_empty_array(),  # 空数组
        17: create_list_array(),  # 列表数组
        18: np.r_[1:4, 0, 4],  # [[1,2,3,0,4]] ,也可以像19一样用。还有很多用法，参考文档。
        # 19: np.c_[1:4, 0, 4],  # 为什么不行呢？
        19: np.c_[np.array([[1, 2, 3]]), 0, 0, np.array([[4, 5, 6]])],
        20: np.logspace(1, 10, num=10, base=2),
        # 此函数返回一个ndarray对象，其中包含在对数刻度上均匀分布的数字。 刻度的开始和结束端点是某个底数的幂，通常为 10。
        # numpy.logscale(start, stop, num, endpoint, base, dtype)
        # 序号	参数及描述
        # 1.	start 起始值是base ** start
        # 2.	stop 终止值是base ** stop
        # 3.	num 范围内的数值数量，默认为50
        # 4.	endpoint 如果为true，终止值包含在输出数组当中
        # 5.	base 对数空间的底数，默认为10
        # 6.	dtype 输出数组的数据类型，如果没有提供，则取决于其它参数
    }.get(create_type, 'error')  # 'error'为默认返回值，可自设置
    # 类switch语句，还可以使用lambda 表达式
    # 参考https://www.cnblogs.com/gerrydeng/p/7191927.html，
    # https://docs.python.org/2/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python


def create_zero_array():
    a = np.arange(6)
    a.astype(np.float)  # 改变数组类型为float
    return np.zeros_like(a)  # 生成一个全0数组，形状和类型与a一致（并不仅限一维数组）.同理ones_like


def create_empty_array():
    a = np.arange(6)
    return np.empty_like(a)  # 生成一个空数组，形状和类型与a一致（并不仅限一维数组）.


def create_list_array():
    demo_list = ['lenovo', 'sansumg', 'moto', 'xiaomi', 'iphone']
    return np.random.choice(demo_list, size=(3, 3))  # 生成3*3大小矩阵，元素在demo_list之间选择。


def array_reshape(x):
    if len(x) == 6:
        pass
    else:
        return
    print '-------------数组变形-------------'
    print '原始数组x（6位）'
    array_print(x)
    x = x.reshape((2, 3))  # x变形为2*3
    print '变形为2*3'
    print x
    print '变为一维'
    print x.ravel()  # np.ravel(x),flatten(x) 同理
    x.shape = (3, 2)

    print '变形为3*2'
    print x
    print '转置'
    x = x.T  # T只适用于一维、二维数组，transpose适用于任何维度，实际上是改变轴，不简单是转置。
    print x
    a = create_array(0)
    print '原始数组a（6位）'
    array_print(a)
    a = np.resize(a, (2, 3))  # 有返回值
    # 不建议使用a.resize((2, 3))
    # reshape：有返回值，所谓有返回值，即不对原始多维数组进行修改；
    # a.resize(2, 3)：无返回值，所谓有返回值，即会对原始多维数组进行修改；
    # b = np.resize(a, (2, 3)) 有返回值
    print '变形为2*3'
    print a
    print 'x和a 按列合并'
    print np.vstack((x, a))  # concatenate（）、stack（）方法也是用来合并数组的。
    print 'x和a 按行合并'
    print np.hstack((x, a))
    a = np.floor(10 * np.random.random((2, 12)))  # floor()返回不大于输入参数的最大整数
    print '原始数组a（2*12）'
    print a
    print '按列平均分为3个数组'
    print np.hsplit(a, 3)  # 同理vsplit
    print '在第3,4列之后切割'
    print np.hsplit(a, (3, 4))  # 同理vsplit
    print '指定轴切割'
    print np.array_split(a, 2, axis=1)  # 按列切割成2组，axis=0 表示按行切割
    print '原始数组a'
    print a
    print 'a沿纵轴左右翻转:'
    print np.fliplr(a)  # 沿纵轴左右翻转
    print 'a沿水平轴上下翻转:'
    print np.flipud(a)  # 沿水平轴上下翻转
    print 'a按照一维顺序滚动位移:'
    print np.roll(a, 2)  # 按照一维顺序滚动位移,移动2位。
    print 'a按照指定轴滚动位移:'
    print np.roll(a, 1, axis=0)  # 按照指定轴滚动位移.0表示上下移动，1表示左右移动。
    print '添加一个轴'
    print np.expand_dims(a, axis=0)
    print '-------------数组变形结束-------------'

    """结果
    -------------数组变形-------------
    原始数组x（6位）
    [0 1 2 3 4 5]
    变形为2*3
    [[0 1 2]
     [3 4 5]]
    变为一维
    [0 1 2 3 4 5]
    变形为3*2
    [[0 1]
     [2 3]
     [4 5]]
    转置
    [[0 2 4]
     [1 3 5]]
    原始数组a（6位）
    [0 1 2 3 4 5]
    变形为2*3
    [[0 1 2]
     [3 4 5]]
    x和a 按列合并
    [[0 2 4]
     [1 3 5]
     [0 1 2]
     [3 4 5]]
    x和a 按行合并
    [[0 2 4 0 1 2]
     [1 3 5 3 4 5]]
    原始数组a（2*12）
    [[ 4.  8.  4.  6.  2.  7.  4.  2.  6.  6.  9.  6.]
     [ 7.  1.  3.  3.  2.  5.  8.  9.  4.  7.  9.  9.]]
    按列平均分为3个数组
    [array([[ 4.,  8.,  4.,  6.],
           [ 7.,  1.,  3.,  3.]]), array([[ 2.,  7.,  4.,  2.],
           [ 2.,  5.,  8.,  9.]]), array([[ 6.,  6.,  9.,  6.],
           [ 4.,  7.,  9.,  9.]])]
    在第3,4列之后切割
    [array([[ 4.,  8.,  4.],
           [ 7.,  1.,  3.]]), array([[ 6.],
           [ 3.]]), array([[ 2.,  7.,  4.,  2.,  6.,  6.,  9.,  6.],
           [ 2.,  5.,  8.,  9.,  4.,  7.,  9.,  9.]])]
    指定轴切割
    [array([[ 4.,  8.,  4.,  6.,  2.,  7.],
           [ 7.,  1.,  3.,  3.,  2.,  5.]]), array([[ 4.,  2.,  6.,  6.,  9.,  6.],
           [ 8.,  9.,  4.,  7.,  9.,  9.]])]
    原始数组a
    [[ 4.  8.  4.  6.  2.  7.  4.  2.  6.  6.  9.  6.]
     [ 7.  1.  3.  3.  2.  5.  8.  9.  4.  7.  9.  9.]]
    a沿纵轴左右翻转:
    [[ 6.  9.  6.  6.  2.  4.  7.  2.  6.  4.  8.  4.]
     [ 9.  9.  7.  4.  9.  8.  5.  2.  3.  3.  1.  7.]]
    a沿水平轴上下翻转:
    [[ 7.  1.  3.  3.  2.  5.  8.  9.  4.  7.  9.  9.]
     [ 4.  8.  4.  6.  2.  7.  4.  2.  6.  6.  9.  6.]]
    a按照一维顺序滚动位移:
    [[ 9.  9.  4.  8.  4.  6.  2.  7.  4.  2.  6.  6.]
     [ 9.  6.  7.  1.  3.  3.  2.  5.  8.  9.  4.  7.]]
    a按照指定轴滚动位移:
    [[ 7.  1.  3.  3.  2.  5.  8.  9.  4.  7.  9.  9.]
     [ 4.  8.  4.  6.  2.  7.  4.  2.  6.  6.  9.  6.]]
    添加一个轴
    [[[ 4.  8.  4.  6.  2.  7.  4.  2.  6.  6.  9.  6.]
      [ 7.  1.  3.  3.  2.  5.  8.  9.  4.  7.  9.  9.]]]
    -------------数组变形结束-------------

    """


def array_print(a, all_print_para=False):
    """
    打印数组
    set_printoptions() 还有很多参数，请参考文档。
    :param a: 数组
    :param all_print_para: 如果为true，则无论数组多大，都要全部打印。
    :return: null
    """
    if all_print_para:
        np.set_printoptions(threshold=np.nan)
    else:
        pass
    print a
    np.set_printoptions(threshold=1000)  # 恢复默认值。threshold表示如果数组元素个数超过1000，使用摘要的方式打印。


def basic_operations(array_operator1, array_operator2):
    """
    数组基本运算
    :param array_operator1: 数组1
    :param array_operator2: 数组2
    :return: null
    """
    """其他操作
    apply_along_axis 自定义数组变换, 
    argmax,最大数的索引
    argmin,最小数的索引 
    argsort/sort, 排序
    bincount()：统计元素出现次数
    ceil/floor,取上界/下界整数
    around(a,decimals),返回四舍五入到所需精度的值.a 输入数组,decimals 要舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
    np.clip(x,3,8) 限制x数组取值范围3-8
    abs/fabs 绝对值。对于非复数，可以使用更快的fabs
    sqrt/square/exp/log/log10/log2/log1p 平方根/平方/指数/自然对数/底数为10的log/底数为2的log
    sign 返回元素的符号：1(正数)、0(零)、-1(负数)
    rint 四舍五入到整数
    modf 返回数组的小数和正数两个独立的数组
    isnan 返回布尔数组，判断是否为数字
    isfinite/isinf 是否有穷/无穷
    cos/cosh/sin/sinh/tan/tanh 普通和双曲三角函数
    add/subtract/multiply/divide/floor_divide 加/减/乘/除/向下圆整除法
    power/pow 第一个数组中的是底数，第二个数组中的是指数
    maximum/fmax/minimum/fmin 最大最小值(fmax/fmin忽略NaN)
    mod 取模/余数
    numpy.real() 返回复数类型参数的实部。
    numpy.imag() 返回复数类型参数的虚部。
    numpy.conj() 返回通过改变虚部的符号而获得的共轭复数。
    numpy.angle() 返回复数参数的角度。 函数的参数是degree。 如果为true，返回的角度以角度制来表示，否则为以弧度制来表示。ex:np.angle(a, deg =  True)
    copysign 将第二个数组中的值的符号复制给第一个数组中
    greater/greater_equal/less/less_equal 元素级比较，产生布尔数组。
    logical_and/logical_or/logical_xor 元素级真值逻辑运算。&、|、^。
    conj 返回所有复数元素的共轭复数,
    corrcoef 求相关矩阵, 
    cov 协方差, 
    var 方差, 方差是偏差的平方的平均值，即mean((x - x.mean())** 2)。 换句话说，标准差是方差的平方根。
    std 计算数组的标准差, 
    cumprod 累乘, 
    cumsum 累加, 
    diff 计算数组的方差,  返回相邻数组元素的差值构成的数组
    mean 计算矩阵的mean均值, 
    ptp()  返回数组最大值和最小值之间的差值
    median 找到数组中的中位数(中间两个数的平均值),  
    percentile()百分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比。
        ex: numpy.percentile(a, q, axis).a 输入数组,q 要计算的百分位数，在 0 ~ 100 之间,axis 沿着它计算百分位数的轴
    trace 方阵的迹, 
    transpose 可以换轴的顺序。
    vdot 两个向量的点积, 对应位置的元素乘积求和
    vectorize 对numpy数组中的每一个元素应用一个函数, 
    where 返回满足条件的数组元素的下标组成的数组  
    average 平均, 
    inner 两个数组的内积, 
    inv 寻找矩阵的乘法逆矩阵, 
    lexsort 按指定行或列的顺序排序, 
    minimum/maximum, 两个数组每个位置的最小/大值（不改变数组格式）
    matmul 两个数组的矩阵积
    determinant 数组的行列式
    solve 求解线性矩阵方程
    nonzero 返回数组a中值不为零的元素的下标,使用方法参考 ：https://www.cnblogs.com/1zhk/articles/4782812.html
    outer 对于多维向量，全部展开变为一维向量，第一个参数表示倍数，使得第二个向量每次变为几倍。http://blog.csdn.net/hqh131360239/article/details/79064592
    prod 连乘, 
    round 返回浮点数x的四舍五入值,  
    re 正则表达式, 
    A.I 矩阵A的逆
    inner 两个数组的内积
    matmul 两个数组的矩阵积
    determinant 数组的行列式
    solve 求解线性矩阵方程
    inv 寻找矩阵的乘法逆矩阵
    """
    print '----------基本操作---------------'
    print 'array_operator1 + array_operator2 = '
    array_print(array_operator1 + array_operator2)  # 支持 +=操作
    print 'array_operator1 - array_operator2 = '
    array_print(array_operator1 - array_operator2)
    print 'array_operator1 ^ 2 = '
    array_print(array_operator1 ** 2)
    print 'array_operator1 * array_operator2（元素积） = '
    array_print(array_operator1 * array_operator2)
    print 'array_operator1 * array_operator2（矩阵积） = '
    array_print(array_operator1.dot(array_operator2))
    print 'array_operator1 * array_operator2（矩阵积） = '
    array_print(np.dot(array_operator1, array_operator2))
    print '10 * sin(array_operator1) = '
    array_print(10 * np.sin(array_operator1))
    print 'array_operator1 <0  的元素结果： '
    array_print(array_operator1 < 0)
    print 'array_operator1 的元素和： '
    array_print(array_operator1.sum())
    print 'array_operator1 最小元素： '
    array_print(array_operator1.min())
    print 'array_operator1 最大元素： '
    array_print(array_operator1.max())
    print 'array_operator1 每列的和： '
    array_print(array_operator1.sum(axis=0))
    print 'array_operator1 每行的最小值： '
    array_print(array_operator1.min(axis=1))
    print 'array_operator1全部是非0空元素？： '
    print np.all(array_operator1)  # 也可以使用下面any的方式
    print 'array_operator1存在非0空元素？： '
    print array_operator1.any()  # 也可以使用上面all的方式
    # any(x)判断x对象是否为空对象，如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true.参数为空返回False"
    # all(x)如果all(x)参数x对象的所有元素不为0、''、False或者x为空对象，则返回True，否则返回False.参数为空返回True"
    print '----------基本操作结束---------------'


def slicing_and_iterating(array_operator):
    """
    切片。
    :return:
    """
    """
    x[1,2,…] 等同于 x[1,2,:,:,:],
    x[…,3] 等同于 x[:,:,:,:,3]
    x[4,…,5,:] 等同 x[4,:,:,5,:].
    """
    print '-------迭代------'
    for row in array_operator:  # 循环每行
        print(row)
    for element in array_operator.flat:  # 循环每个元素
        print(element)
    for element in np.nditer(array_operator, op_flags=['readwrite']):  # 循环每个元素，读写模式。默认为只读模式。还有只写模式。
        print element
    print '-------切片------'
    a = np.arange(12) ** 2

    print ('初始数组')
    print a
    print '使用list做索引'
    a[[1, 3, 4]] = 0  # a[[0,0,2]]=[1,2,3],但是不要使用+=，容易出错
    print ('将1，3,4赋值为0')
    print a
    i = np.array([1, 1, 3, 8, 5])
    print ('读取1, 1, 3, 8, 5位')
    print a[i]

    print ('使用二维list作为索引')
    palette = np.array([[0, 0, 0],  # black
                        [255, 0, 0],  # red
                        [0, 255, 0],  # green
                        [0, 0, 255],  # blue
                        [255, 255, 255]])  # white
    image = np.array([[0, 1, 2, 0],
                      [0, 3, 4, 0]])
    print palette[image]
    print '使用list作为多维索引'
    a = np.arange(12).reshape(3, 4)
    print a
    i = np.array([[0, 1],
                  [1, 2]])
    j = np.array([[2, 1],
                  [3, 3]])
    print ('两个索引')
    print a[i, j]
    print ('一个索引')
    print a[i, 2]
    print 'bool索引'
    a = np.arange(12).reshape(3, 4)
    b = a > 4
    print ('bool list')
    print b
    print ('a[b]=')
    print a[b]
    a[b] = 0
    print ('a[b]=0 赋值')
    print a
    a = a.ravel()
    print '把a变为一维数组'
    print a
    s = slice(2, 7, 2)
    print '读取2-7之间，每2位取一个数'
    print a[s]
    print '-------切片结束------'
    """
    -------切片------
    初始数组
    [  0   1   4   9  16  25  36  49  64  81 100 121]
    使用list做索引
    将1，3,4赋值为0
    [  0   0   4   0   0  25  36  49  64  81 100 121]
    读取1, 1, 3, 8, 5位
    [ 0  0  0 64 25]
    使用二维list作为索引
    [[[  0   0   0]
      [255   0   0]
      [  0 255   0]
      [  0   0   0]]
    
     [[  0   0   0]
      [  0   0 255]
      [255 255 255]
      [  0   0   0]]]
    使用list作为多维索引
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    两个索引
    [[ 2  5]
     [ 7 11]]
    一个索引
    [[ 2  6]
     [ 6 10]]
    bool索引
    bool list
    [[False False False False]
     [False  True  True  True]
     [ True  True  True  True]]
    a[b]=
    [ 5  6  7  8  9 10 11]
    a[b]=0 赋值
    [[0 1 2 3]
     [4 0 0 0]
     [0 0 0 0]]
     把a变为一维数组
    [0 1 2 3 4 0 0 0 0 0 0 0]
    读取2-7之间，每2位取一个数
    [2 4 0]
    -------切片结束------
    """


def copies_and_views(array_operator):
    """
    复制和视图。分三类1、赋值，相当于是一个指针。2、浅拷贝，共享数据，不共享结构、属性，相当于视图。3、深拷贝，数据相同，不共享任何东西。
    :param array_operator:原始数组
    :return:
    """
    print '-------复制和视图---------'
    print '原始数组'
    print array_operator
    print '原始形状'
    print array_operator.shape
    print '####赋值####'
    b = array_operator  # no new object is created
    print '打印b'
    print b
    print '是否是同一数组'
    print b is array_operator  # a and b are two names for the same ndarray object
    print '修改b的形状为2*3，打印原始数组形状'
    b.shape = 2, 3
    # 如果使用 b = b.reshape((2, 3))，则只改变b的形状,因为reshape返回一个新的数组，相当于b被重新赋值了。已经和array_operator没有关系了。
    print array_operator.shape

    print '####浅复制####'
    print '打印c是否是array_operator'
    c = array_operator.view()
    print c is array_operator
    print '打印c的原始数组是否是array_operator'
    print c.base is array_operator  # c is a view of the data owned by a
    print 'c变形为3*2，打印array_operator形状'
    c.shape = 3, 2  # a's shape doesn't change
    print array_operator.shape
    print 'c[2, 0] = 1234 ，打印array_operator'
    c[2, 0] = 1234  # a's data changes
    print array_operator
    print '利用新数组s改变0、1列的值，打印array_operator'
    s = array_operator[:, 0:2]  # spaces added for clarity; could also be written "s = a[:,1:3]"
    s[:] = 10  # s[:] is a view of s. Note the difference between s=10 and s[:]=10
    print array_operator

    print '####深复制####'
    d = array_operator.copy()  # a new array object with new data is created
    print '打印d是否是array_operator'
    print d is array_operator
    print '打印d的原始数组是否是array_operator'
    print d.base is array_operator  # d doesn't share anything with a
    print 'd[0, 0] = 1234 ，打印array_operator'
    d[0, 0] = 9999
    print array_operator

    print '-------复制和视图结束---------'
    """结果
    -------复制和视图---------
    原始数组
    [0 1 2 3 4 5]
    原始形状
    (6L,)
    ####赋值####
    打印b
    [0 1 2 3 4 5]
    是否是同一数组
    True
    修改b的形状为2*3，打印原始数组形状
    (2L, 3L)
    ####浅复制####
    打印c是否是array_operator
    False
    打印c的原始数组是否是array_operator
    True
    c变形为3*2，打印array_operator形状
    (2L, 3L)
    c[2, 0] = 1234 ，打印array_operator
    [[   0    1    2]
     [   3 1234    5]]
    利用新数组s改变0、1列的值，打印array_operator
    [[10 10  2]
     [10 10  5]]
    ####深复制####
    打印d是否是array_operator
    False
    打印d的原始数组是否是array_operator
    False
    d[0, 0] = 1234 ，打印array_operator
    [[10 10  2]
     [10 10  5]]
    -------复制和视图结束---------
    (2L, 3L)
    """


def array_change():
    """
    几种数据类型的转换。
    :return:
    """
    print '------数组、列表、矩阵转换示例------'
    print '原始列表'
    a1 = [[1, 2, 3], [4, 5, 6]]  # 列表
    print type(a1)
    print a1
    print '转换成数组'
    a2 = np.array(a1)  # 列表转数组
    print type(a2)
    print a2
    print '转换成数组(第二种方法)'
    a = np.asarray(a1)
    print type(a)
    print a
    print '列表转成矩阵'
    a3 = np.mat(a1)  # 列表转矩阵
    print type(a3)
    print a3

    print '数组转列表'
    a4 = a2.tolist()  # 数组转列表
    print type(a4)
    print a4
    print '矩阵转列表'
    a5 = a3.tolist()  # 矩阵转列表
    print type(a5)
    print a5
    print '两次转换后是否一致：'
    print a4 == a5
    # True
    print '------数组、列表、矩阵转换示例------'
    """
    ------数组、列表、矩阵转换示例------
    原始列表
    <type 'list'>
    [[1, 2, 3], [4, 5, 6]]
    转换成数组
    <type 'numpy.ndarray'>
    [[1 2 3]
     [4 5 6]]
    转换成数组(第二种方法)
    <type 'numpy.ndarray'>
    [[1 2 3]
     [4 5 6]]
    列表转成矩阵
    <class 'numpy.matrixlib.defmatrix.matrix'>
    [[1 2 3]
     [4 5 6]]
    数组转列表
    <type 'list'>
    [[1, 2, 3], [4, 5, 6]]
    矩阵转列表
    <type 'list'>
    [[1, 2, 3], [4, 5, 6]]
    两次转换后是否一致：
    True
    ------数组、列表、矩阵转换示例------
    """


def diff_matrix_array():
    """
    比较矩阵和数组
    :return:
    """
    print '-----------比较矩阵和数组---------'
    a = np.arange(12)
    a.shape = (3, 4)
    m = np.mat(a.copy())
    print 'A='
    print a
    print 'M='
    print m
    print 'A[:, 1]'
    print a[:, 1]
    print 'A[:, 1].shape'
    print a[:, 1].shape
    print 'M[:, 1]'
    print m[:, 1]
    print 'M[:, 1].shape'
    print m[:, 1].shape
    a.shape = (4, 4)
    matrix = np.mat(a)
    print '矩阵matrix'
    print matrix
    print '对应行列式的值'
    print np.linalg.det(matrix)  # 求矩阵的行列式值，0
    print 'matrix的秩'
    print np.linalg.matrix_rank(matrix)  # 求矩阵的秩，2，不满秩，因为行与行之间等差
    print '-----------比较矩阵和数组结束---------'
    """
    -----------比较矩阵和数组---------
    A=
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    M=
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    A[:, 1]
    [1 5 9]
    A[:, 1].shape
    (3L,)
    M[:, 1]
    [[1]
     [5]
     [9]]
    M[:, 1].shape
    (3L, 1L)
    矩阵matrix
    [[4]]
    对应行列式的值
    4.0
    matrix的秩
    1
    -----------比较矩阵和数组结束---------
    """


def random_example():
    """
    numpy随机模块包含了随机数产生和统计分布相关的基本函数，Python本身也有随机模块random，不过numpy功能更丰富。
    本方法来源https://zhuanlan.zhihu.com/p/24309547。未测试。
    :return:
    """
    # 设置随机数种子
    random.seed(42)

    # 产生一个1x3，[0,1)之间的浮点型随机数
    # array([[ 0.37454012,  0.95071431,  0.73199394]])
    # 后面的例子就不在注释中给出具体结果了
    random.rand(1, 3)

    # 产生一个[0,1)之间的浮点型随机数
    random.random()

    # 下边4个没有区别，都是按照指定大小产生[0,1)之间的浮点型随机数array，不Pythonic…
    random.random((3, 3))
    random.sample((3, 3))
    random.random_sample((3, 3))
    random.ranf((3, 3))

    # 产生10个[1,6)之间的浮点型随机数
    5 * random.random(10) + 1
    random.uniform(1, 6, 10)

    # 产生10个[1,6)之间的整型随机数
    random.randint(1, 6, 10)

    # 产生2x5的标准正态分布样本
    random.normal(size=(5, 2))

    # 产生5个，n=5，p=0.5的二项分布样本
    random.binomial(n=5, p=0.5, size=5)

    a = np.arange(10)

    # 从a中有回放的随机采样7个
    random.choice(a, 7)

    # 从a中无回放的随机采样7个
    random.choice(a, 7, replace=False)

    # 对a进行乱序并返回一个新的array
    a = random.permutation(a)

    # 对a进行in-place乱序
    random.shuffle(a)

    # 生成一个长度为9的随机bytes序列并作为str返回
    # '\x96\x9d\xd1?\xe6\x18\xbb\x9a\xec'
    random.bytes(9)


def element_operate():
    """
    数组对元素 添加、插入、删除、去重操作
    :return:
    """
    print '------元素操作------'
    a = np.array([[1, 2, 3], [4, 5, 6]])

    print '（添加）第一个数组：'
    print a
    print '\n'

    print '向数组添加元素：'
    print np.append(a, [7, 8, 9])
    print '\n'

    print '沿轴 0 添加元素：'
    print np.append(a, [[7, 8, 9]], axis=0)
    print '\n'

    print '沿轴 1 添加元素：'
    print np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1)

    print '（插入）第一个数组：'
    print '未传递 Axis 参数。 在插入之前输入数组会被展开。'
    print np.insert(a, 3, [11, 12])
    print '\n'
    print '传递了 Axis 参数。 会广播值数组来配输入数组。'

    print '沿轴 0 广播：'
    print np.insert(a, 1, [11], axis=0)
    print '\n'

    print '沿轴 1 广播：'
    print np.insert(a, 1, [11], axis=1)

    print '（删除）第一个数组：'
    print a
    print '\n'

    print '未传递 Axis 参数。 在插入之前输入数组会被展开。'
    print np.delete(a, 5)
    print '\n'

    print '删除第二列：'
    print np.delete(a, 1, axis=1)
    print '\n'

    print '包含从数组中删除的替代值的切片：'
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print np.delete(a, np.s_[::2])

    print '（去重）第一个数组：'
    print a
    print '\n'

    print '第一个数组的去重值：'
    u = np.unique(a)
    print u
    print '\n'

    print '去重数组的索引数组：'
    u, indices = np.unique(a, return_index=True)
    print indices
    print '\n'

    print '我们可以看到每个和原数组下标对应的数值：'
    print a
    print '\n'

    print '去重数组的下标：'
    u, indices = np.unique(a, return_inverse=True)
    print u
    print '\n'

    print '下标为：'
    print indices
    print '\n'

    print '使用下标重构原数组：'
    print u[indices]
    print '\n'

    print '返回去重元素的重复数量：'
    u, indices = np.unique(a, return_counts=True)
    print u
    print indices

    a = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
    print '我们的数组是：'
    print a
    print '\n'
    print '查找非0元素索引：'
    print np.nonzero(a)

    print '------元素操作结束------'
    """
    ------元素操作------
    （添加）第一个数组：
    [[1 2 3]
     [4 5 6]]
    
    
    向数组添加元素：
    [1 2 3 4 5 6 7 8 9]
    
    
    沿轴 0 添加元素：
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    
    
    沿轴 1 添加元素：
    [[1 2 3 5 5 5]
     [4 5 6 7 8 9]]
    （插入）第一个数组：
    未传递 Axis 参数。 在插入之前输入数组会被展开。
    [ 1  2  3 11 12  4  5  6]
    
    
    传递了 Axis 参数。 会广播值数组来配输入数组。
    沿轴 0 广播：
    [[ 1  2  3]
     [11 11 11]
     [ 4  5  6]]
    
    
    沿轴 1 广播：
    [[ 1 11  2  3]
     [ 4 11  5  6]]
    （删除）第一个数组：
    [[1 2 3]
     [4 5 6]]
    
    
    未传递 Axis 参数。 在插入之前输入数组会被展开。
    [1 2 3 4 5]
    
    
    删除第二列：
    [[1 3]
     [4 6]]
    
    
    包含从数组中删除的替代值的切片：
    [ 2  4  6  8 10]
    （去重）第一个数组：
    [ 1  2  3  4  5  6  7  8  9 10]
    
    
    第一个数组的去重值：
    [ 1  2  3  4  5  6  7  8  9 10]
    
    
    去重数组的索引数组：
    [0 1 2 3 4 5 6 7 8 9]
    
    
    我们可以看到每个和原数组下标对应的数值：
    [ 1  2  3  4  5  6  7  8  9 10]
    
    
    去重数组的下标：
    [ 1  2  3  4  5  6  7  8  9 10]
    
    
    下标为：
    [0 1 2 3 4 5 6 7 8 9]
    
    
    使用下标重构原数组：
    [ 1  2  3  4  5  6  7  8  9 10]
    
    
    返回去重元素的重复数量：
    [ 1  2  3  4  5  6  7  8  9 10]
    [1 1 1 1 1 1 1 1 1 1]
    我们的数组是：
    [[30 40  0]
     [ 0 20 10]
     [50  0 60]]
    
    
    查找非0元素索引：
    (array([0, 0, 1, 1, 2, 2], dtype=int64), array([0, 1, 1, 2, 0, 2], dtype=int64))
    ------元素操作结束------
    """


def bin_operate():
    """
    位操作
    :return:
    """
    print '------位运算--------'

    print '13 和 17 的二进制形式：'
    a, b = 13, 17
    print bin(a), bin(b)
    print '\n'

    print '13 和 17 的位与：'
    print np.bitwise_and(13, 17)

    print '13 和 17 的位或：'
    print np.bitwise_or(13, 17)

    print '13 的位反转，其中 ndarray 的 dtype 是 uint8：'
    print np.invert(np.array([13], dtype=np.uint8))
    print '\n'
    # 比较 13 和 242 的二进制表示，我们发现了位的反转

    print '13 的二进制表示：'
    print np.binary_repr(13, width=8)
    print '\n'

    print '242 的二进制表示：'
    print np.binary_repr(242, width=8)

    print '将 10 左移两位：'
    print np.left_shift(10, 2)
    print '\n'

    print '10 的二进制表示：'
    print np.binary_repr(10, width=8)
    print '\n'

    print '40 的二进制表示：'
    print np.binary_repr(40, width=8)
    #  '00001010' 中的两位移动到了左边，并在右边添加了两个 0。

    print '将 40 右移两位：'
    print np.right_shift(40, 2)
    print '\n'

    print '40 的二进制表示：'
    print np.binary_repr(40, width=8)
    print '\n'

    print '10 的二进制表示：'
    print np.binary_repr(10, width=8)
    #  '00001010' 中的两位移动到了右边，并在左边添加了两个 0。
    print '------位运算结束--------'
    """
    ------位运算--------
    13 和 17 的二进制形式：
    0b1101 0b10001
    
    
    13 和 17 的位与：
    1
    13 和 17 的位或：
    29
    13 的位反转，其中 ndarray 的 dtype 是 uint8：
    [242]
    
    
    13 的二进制表示：
    00001101
    
    
    242 的二进制表示：
    11110010
    将 10 左移两位：
    40
    
    
    10 的二进制表示：
    00001010
    
    
    40 的二进制表示：
    00101000
    将 40 右移两位：
    10
    
    
    40 的二进制表示：
    00101000
    
    
    10 的二进制表示：
    00001010
    ------位运算结束--------
    """


def string_operate():
    """
    字符串操作
    """
    print '----------字符串操作-------------------'
    print '连接两个字符串：'
    print np.char.add(['hello'], [' xyz'])
    print '\n'

    print '连接示例：'
    print np.char.add(['hello', 'hi'], [' abc', ' xyz'])

    print '字符串重复'
    print np.char.multiply('Hello ', [3])

    print '字符串两侧填充'
    print np.char.center('hello', 20, fillchar='*')

    print '首字母大写'
    print np.char.capitalize('hello world')

    print '所有单词首字母大写'
    print np.char.title('hello how are you?')

    print '所有字母转小写'  # upper() 大写
    print np.char.lower(['HELLO', 'WORLD'])
    print np.char.lower('HELLO')

    print '返回输入字符串中的单词列表'  # 默认情况下，空格用作分隔符。 否则，指定的分隔符字符用于分割字符串。
    print np.char.split('hello how are you?')
    print np.char.split('TutorialsPoint,Hyderabad,Telangana', sep=',')

    print '返回数组中元素的单词列表，以换行符分割。'
    print np.char.splitlines('hello\nhow are you?')

    print '返回数组的副本，其中元素移除了开头或结尾处的特定字符。'
    print np.char.strip('ashok arora', 'a')
    print np.char.strip(['arora', 'admin', 'java'], 'a')

    print '返回一个字符串，其中单个字符由特定的分隔符连接。'
    print np.char.join(':', 'dmy')
    print np.char.join([':', '-'], ['dmy', 'ymd'])

    print '返回字符串副本，其中所有字符序列的出现位置都被另一个给定的字符序列取代。'
    print np.char.replace('He is a good boy', 'is', 'was')

    print '在给定的字符串中使用特定编码'
    a = np.char.encode('hello', 'cp500')
    print a
    print '使用特定编码解码字符串'
    print np.char.decode(a, 'cp500')

    """ http://blog.csdn.net/qq_34162294/article/details/53727357
        *首先要搞清楚，字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，
        即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
        decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
        encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
        总得意思:想要将其他的编码转换成utf - 8
        必须先将其解码成unicode然后重新编码成utf - 8, 它是以unicode为转换媒介的
        如：s = '中文'
        如果是在utf8的文件中，该字符串就是utf8编码，如果是在gb2312的文件中，则其编码为gb2312。这种情况下，要进行编码转换，都需要先用
        decode方法将其转换成unicode编码，再使用encode方法将其转换成其他编码。通常，在没有指定特定的编码方式时，都是使用的系统默认编码创建的代码文件。
        如下：
        s.decode('utf-8').encode('utf-8')
        decode():是解码
        encode()：是编码
        isinstance(s, unicode):判断s是否是unicode编码，如果是就返回true, 否则返回false *
    """
    print sys.getdefaultencoding()

    s = u'中文'
    if isinstance(s, unicode):   # 如果是unicode就直接编码不需要解码
        print '打印‘中文’的utf-8编码'
        print s.encode('utf-8')
    else:
        print '打印‘中文’的gb2312编码'
        print s.decode('utf-8').encode('gb2312')

    print '系统编码'
    print sys.getdefaultencoding()    # 获取系统默认的编码
    reload(sys)
    sys.setdefaultencoding('utf8')    # 修改系统的默认编码
    print '修改后的系统编码'
    print sys.getdefaultencoding()
    print '----------字符串操作结束-------------------'
    """
    ----------字符串操作-------------------
    连接两个字符串：
    ['hello xyz']
    
    
    连接示例：
    ['hello abc' 'hi xyz']
    字符串重复
    Hello Hello Hello 
    字符串两侧填充
    *******hello********
    首字母大写
    Hello world
    所有单词首字母大写
    Hello How Are You?
    所有字母转小写
    ['hello' 'world']
    hello
    返回输入字符串中的单词列表
    ['hello', 'how', 'are', 'you?']
    ['TutorialsPoint', 'Hyderabad', 'Telangana']
    返回数组中元素的单词列表，以换行符分割。
    ['hello', 'how are you?']
    返回数组的副本，其中元素移除了开头或结尾处的特定字符。
    shok aror
    ['ror' 'dmin' 'jav']
    返回一个字符串，其中单个字符由特定的分隔符连接。
    d:m:y
    ['d:m:y' 'y-m-d']
    返回字符串副本，其中所有字符序列的出现位置都被另一个给定的字符序列取代。
    He was a good boy
    在给定的字符串中使用特定编码
    �����
    使用特定编码解码字符串
    hello
    ascii
    打印‘中文’的utf-8编码
    中文
    系统编码
    ascii
    修改后的系统编码
    utf8
    ----------字符串操作结束-------------------
    """


def sort_element():
    """
    排序算法。
    :return:
    """

    """
    sort()函数返回输入数组的排序副本。 它有以下参数：
    numpy.sort(a, axis, kind, order)
    序号	参数及描述
    1.	a 要排序的数组
    2.	axis 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序
    3.	kind 默认为'quicksort'（快速排序）
    4.	order 如果数组包含字段，则是要排序的字段

    """
    print '--------排序算法---------'
    a = np.array([[3, 7], [9, 1]])
    print '我们的数组是：'
    print a
    print '\n'
    print '调用 sort() 函数：'
    print np.sort(a)
    print '\n'
    print '沿轴 0 排序：'
    print np.sort(a, axis=0)
    print '\n'
    # 在 sort 函数中排序字段
    dt = np.dtype([('name', 'S10'), ('age', int)])
    a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
    print '我们的数组是：'
    print a
    print '\n'
    print '按 name 排序：'
    print np.sort(a, order='name')

    x = np.array([3, 1, 2])
    print '我们的数组是：'
    print x
    print '\n'
    print '对 x 调用 argsort() 函数：'

    # numpy.argsort()函数对输入数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。 这个索引数组用于构造排序后的数组。
    y = np.argsort(x)
    print y
    print '\n'
    print '以排序后的顺序重构原数组：'
    print x[y]
    print '\n'
    print '使用循环重构原数组：'
    for i in y[0]:
        print x[i],

    # 使用键序列执行间接排序。 键可以看作是电子表格中的一列。 该函数返回一个索引数组，使用它可以获得排序数据。 注意，最后一个键恰好是 sort 的主键。
    print 'lexsort()'
    nm = ('raju', 'anil', 'ravi', 'amar')
    dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
    ind = np.lexsort((dv, nm))
    print '调用 lexsort() 函数：'
    print ind
    print '\n'
    print '使用这个索引来获取排序后的数据：'
    print [nm[i] + ", " + dv[i] for i in ind]
    print '--------排序算法结束---------'
    """
    --------排序算法---------
    我们的数组是：
    [[3 7]
     [9 1]]
    
    
    调用 sort() 函数：
    [[3 7]
     [1 9]]
    
    
    沿轴 0 排序：
    [[3 1]
     [9 7]]
    
    
    我们的数组是：
    [('raju', 21) ('anil', 25) ('ravi', 17) ('amar', 27)]
    
    
    按 name 排序：
    [('amar', 27) ('anil', 25) ('raju', 21) ('ravi', 17)]
    我们的数组是：
    [3 1 2]
    
    
    对 x 调用 argsort() 函数：
    [1 2 0]
    
    
    以排序后的顺序重构原数组：
    [1 2 3]
    
    
    使用循环重构原数组：
    1 2 3 lexsort()
    调用 lexsort() 函数：
    [3 1 0 2]
    
    
    使用这个索引来获取排序后的数据：
    ['amar, f.y.', 'anil, s.y.', 'raju, f.y.', 'ravi, s.y.']
    --------排序算法结束---------

    """


def file_oper(arr):
    """
    文件操作。numpy有很多文件操作方法。未详细展开。
    :param arr: 要写入的数组
    :return:
    """
    # arr = np.load('p.npy')  # 从文中间读取数组
    np.save('p.npy', arr)  # 保存数组arr到文件p.npy.npy是Numpy专用的二进制格式保存文件


def main():
    print chardet.detect('初始数组')  # 测试编码。{'confidence': 0.938125, 'language': '', 'encoding': 'utf-8'} 置信度：0.938125
    array_attribute(create_array(0))
    basic_operations(create_array(10), create_array(1))
    array_reshape(create_array(0))
    file_oper(create_array(0))

    """以下三行是一组"""
    a = create_array(0)
    copies_and_views(a)
    print a.shape  # 如果把数组当做参数传递，传递的是指针。注意函数内部和外部形状的输出结果

    slicing_and_iterating(create_array(0))
    diff_matrix_array()
    array_change()
    element_operate()
    bin_operate()
    string_operate()
    sort_element()


if __name__ == '__main__':
    main()
