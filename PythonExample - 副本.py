from functools import partial
import math
from string import Template
from cgi import FieldStorage as fs  # 定义别名
import re
#TODO 单步调试
"""
* 转移字符：
\n 换行

* 不同的缩进代表不同的级别
建议：设置ide的tab自动转换为空格。File--->setting,选择Editor--->python  设置Tab size 为4
可以设置ide显示空格为一个点。View--->Active--->Show Whitespaces

* __doc__ p46-47
* http://blog.csdn.net/fengjiexyb/article/details/77852567
"""
# TODO 编码问题


def fun_sequence():
    """
    序列包括：字符串、列表、元组(tuple)。内部元素有序排列。
    字符串、元组不可改变其中的内容，    列表可以
    字符串数据类型必须一致，    元组、列表可以不一致


    :return:
    """

    a = [1, 2, 3]  # 列表
    b = 'this is a string.'  # 字符串
    tuple = (['a', 'b'], 2, 3)
    print b[3]
    print a * 3  # 重复
    print a + a  # 连接
    print 1 in a  # 判断是否存在该元素
    print 'c' not in b
    fun_slice(b)
    print cmp(a, [1, 2])
    print cmp(b, 'this is')  # 按acsii比较
    print len(a)
    print max(b)  # min()
    for i, char in enumerate(b):
        print i, char
    str1, str2 = 'abcd', 'xyz'
    print zip(str1, str2)  # 两个字符串中的字符，一一对应
    print sorted(b, reverse=False)  # 逆序排序，第二个参数可以省略
    print sum(a)  # 注意;只对数值型有效
    for char in reversed(a):  # reversed 逆序
        print char
    list_oper(a)
    string_template('python')
    tuple_no_change(tuple)


def tuple_no_change(tuple):  # 无返回值的函数返回类型为None，不是void。多个返回值实际上返回的是一个元组。
    """
    元组元素不可变，不等于元素内的元素不可变
    :param tuple:
    :return:
    """
    tuple[0][1] = z
    print tuple


def string_template(parm):
    """
    字符串模板
    :param parm:
    :return:
    """
    s_template = Template('There is a ${parm} template.')
    print s_template.substitute(parm=parm)
    print s_template.safe_substitute()


def list_oper(list1):
    list1.append(1)  # 添加一个元素
    print list1.count(2)  # 统计2出现次数
    print list1.extend('123')  # 添加一个序列
    print list1.index(3, 0, 4)  # 在list1中找到3，返回索引值。索引值要大于等于0，小于4.后两个参数可以省略。
    print list1.pop(1)  # 删除并返回位置1的元素。默认值为最后一个元素。
    list1.pop()  # 删除最后一个数，
    print list1.reverse()  # 翻转
    del list1[1]  # 删除指定下标元素
    sorted(list1)  # 返回新的list
    list1.sort()  # 修改本身

    # zip()函数单个参数
    list1 = [1, 2, 3, 4]
    tuple1 = zip(list1)
    # 打印zip函数的返回类型
    print("zip()函数的返回类型：\n", type(tuple1))
    # 将zip对象转化为列表
    print("zip对象转化为列表：\n", list(tuple1))
    '''这部分适合于3.5版本之上
    ## *zip()函数
    print('=*' * 10 + "*zip()函数" + '=*' * 10)
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
    print("*zip(m, n)返回:\n", *zip(m, n))
    m2, n2 = zip(*zip(m, n))
    # 若相等，返回True；说明*zip为zip的逆过程
    print(m == list(m2) and n == list(n2))
    '''
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [4, 5, 6, 7, 8]
    zipped = zip(a, b)     # 打包为元组的列表
    # [(1, 4), (2, 5), (3, 6)]
    zip(a, c)              # 元素个数与最短的列表一致
    # [(1, 4), (2, 5), (3, 6)]
    zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式
    # [(1, 2, 3), (4, 5, 6)]


def fun_slice(seq):
    """
    切片操作
    :param seq:
    :return:
    """
    print seq[1:7]  # 读取从第一个元素到第（7-1）个元素间的所有元素，从0开始编码。
    print seq[2:]  # 读取第二个元素（含）之后的所有元素
    print seq[2::2]  # 读取第二个元素（含）之后的元素,隔一个读一个（即：间隔2-1)。
    print seq[-5]  # 读取倒数第五个元素。
    print seq[::-1]  # 逆序


def fun_example(parameter):  # 定义一个函数（方法）
    """
    方法注释。一般写在方法内部。双引号标识。
    方法名、变量名，一般不使用大小写方式，推荐使用下划线分割多个单词。
    方法前要空两行。
    :param parameter:  # 参数声明不需要写数据类型
    :return:
    """
    print parameter


def main():
    str = 'adfhgdhfgdh' \
        'fghdsjf'
    # 不建议每行超过120个字符。如果确实需要，可以使用'\'来分行
    str += '''kdhfdsf 
    jdhfsdhfk
    sdgfjdsh'''  # 三个单引号表示的字符串，在引号内部可以换行。
    str += ('a'
            'b')  # 和'\'相比，推荐使用括号方式换行
    print str
    x, y, z = 1, 2, 'string'
    x, y = y, x
    print x, y, z
    # method_name()
    x = 4
    print type(x)
    print id(x)
    y = x
    print x is y

    """
    Python 没有 char类型，byte类型，指针，不区分float、double
    """
    print 1/2
    print 1.0/2.0
    print 3**2
    print pow(3, 2)  # 和** 一致，早期存在三个参数函数。
    print 1.0//2.0
    print 1 % 2
    print round(7.14)  # 最近接原数的整数
    print math.floor(7.9)   # 向下取整
    print int(7.9)  # 取整


def method_name():
    pass  # 单行注释。‘#’之前空两格，之后空一格。
    # pass表示空语句
    word = raw_input('Enter a word:')  # 单引号、双引号、三个单引号都可以表示字符串。三引号内部可以有换行符、制表符
    # 变量名大小写敏感。变量名包含字符：数字、字母、下划线，字母开头8
    # 等号两端加一个空格。（一般运算符两端都建议加空格，参数不算）   ###TODO 参数带等号
    # raw _input 从控制台读取数据
    print word
    print "this is a %dth input word: %s!" % (1, word)  # 输出语句。如果只有一个参数不需要括号。###todo 格式化输出例子
    # 逗号后面建议加一空格
    # TODO 格式化输出
    # TODO help() 需要交互式解释器？？
    # fixme 需要修改的bug
    # TODO， 未完成的功能


def fun_dict():
    adict = {'ip': '200.100.100.191', 'port': 80}  # dict是无序的。如果需要有序可以用OrderedDict
    print adict
    bdict = {}.fromkeys(('x', 'y'), -1)
    print bdict
    cdict = {}.fromkeys(('x', 'y'))
    print cdict
    fdict = {}.fromkeys(('xyz'), -1)
    print fdict
    for key in adict.keys():  # 可以省略keys（）
        print key, adict[key]  # 不能使用adict[1]方式
    print 'ip' in adict
    print 'ip' not in bdict
    adict[1] = 'add'  # 新增条目
    print cmp(adict, bdict)  # 比较顺序：依次比较字典长度，字典的键，字典的值，完全相同返回0
    ddict = dict([['x', 1], ['y', 2]])
    print ddict
    edict = dict([('xy'[i-1], i) for i in range(1, 3)])  # todo arange和range的区别？dict的元素顺序？
    print edict
    print len(edict)
    print hash('hash')  # 返回hash值
    print adict.keys()
    print adict.values()
    print adict.items()
    adict.pop(index)  # 删除给定健对应的值，
    adict.clear()  # 清空字典内容
    adict.popitem()  # 随机删除字典内容


def fun_set():
    # set没有重复记录
    s = set('dfgkfdjh')
    print s
    s2 = frozenset('book')  # frozenset不能用update,add
    print 'b' in s2
    print 'b' not in s2
    print s2
    for i in s2:
        print i
    s.add('z')
    s.update('desk')  # 只添加s中没有的字母,
    print s
    s.remove('d')
    print s
    s -= set('pay')
    print s
    # 以下四种操作可以和等号连用，如上所示。
    print s | s2  # 并集
    print s & s2  # 交集
    print s - s2  # 差补（相对补集）
    print s ^ s2  # 异或


def fun_iffor(a):
    if a is True:
        print 'a'
    elif a == 'aa':
        print 'aa'
    else:
        print 'else'
    x = 1
    y = 2
    smller = x if x < y else y
    print smller
    list1 = ['a', 's', 'd', 'f']
    for i, each in enumerate(list1):   # 可以用while语句、break、continue
        print i, each
    for i in range(2, 19, 3):  # 第一个参数默认为0，第三个参数默认为1。生成序列不包括第二个参数
        # range会直接生成一个list对象。而xrange则不会直接生成一个list，而是每次调用返回其中的一个值。所以xrange做循环的性能比range好，尤其是返回很大的时候！
        print i
    num = 100
    count = num/2
    while count > 1:
        if num % count == 0:
            break  # 如果执行break，也会跳过else的
        count -= 1
    else:  # 在while之后在运行else。for语句也可以配合else
        print 'is'
    mylist = ['a', 's', 'd']
    i = iter(mylist)
    print i.next()
    print i.next()
    print [x ** 2 for x in range(4)]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print [x for x in list2 if x % 2]
    print filter(lambda parm : parm % 2, list2)
     #  lambda 后面的x表示输入的参数（任意个），冒号后面的是函数体。
    # filter的第一个参数是过滤器函数，如果返回为真（1）则保留，返回为假（0) 被过滤，第二个参数是准备过滤的数据。


def shelveSerializable():
    """序列化"""
    '''这种方式在python2.7中会有异常：AttributeError: DbfilenameShelf instance has no attribute '__exit__'
    # 保存数据到student文件
    with shelve.open('student') as db:
        db['name'] = 'Tom'
        db['age'] = 19
        db['hobby'] = ['篮球', '看电影', '弹吉他']
        db['other_info'] = {'sno': 1, 'addr': 'xxxx'}

    # 读取数据
    with shelve.open('student') as db:
        for key, value in db.items():
            print(key, ': ', value)
    '''
    s = shelve.open("test_shelve")
    s["name"] = "DaLian"
    s["neusoft"] = "HHH"
    s.close()

    f = shelve.open("test_shelve")#如果上面没有关闭，但是文件存在，就会读取以前的文件，而不是上面的新文件。
    print(f.get("name"))
    print(f.get("neusoft"))

    f["neusoft"] = "sss" #可以修改
    f["soft"] = [1,2]  #可以添加
    print(f.get("neusoft"))
    print(f.get("soft"))
    f["soft"].append(3) #但是追加，还是会显示追加前的数据
    print(f.get("soft"))
    f.writeback = True #设置回写，也可以在打开文件时设置
    f["soft"].append(4) #现在就可以追加了
    print(f.get("soft"))


def pickle_serializable():
    """pickle序列化"""
    li = [1, 2, 3, 4, 5]
    pw = open('pickleSerializable', 'wb')
    pw.write(pickle.dumps(li))
    pw.close()

    #反序列化
    li = json.load(open("pickleSerializable", "r"))
    print(li, type(li))


'''json序列化'''
def jsonSerializable():
    dic = {'k1': 'v1'}
    print(dic, type(dic))
    # json.dumps 把python的基本数据类型转换成字符串形式
    result = json.dumps(dic)
    print(dic, type(result))

    # 反序列化
    s1 = '{"k1":123}'
    # json.loads 把字符串形式转换成其他基本数据类型
    # 注意： 反序列化时，中间字符串一定用""表示，原因：跨语言操作时，其他语言是用""表示字符串
    dic1 = json.loads(s1)
    print(dic1, type(dic1))

    # 序列化并把内容写进文本
    # 也可以写成pickle例子的形式
    li = [1, 2, 3, 4, 5]
    json.dump(li, open("test", "w"))

    # 从文本读出字符串并进行反序列化，但文件中的内容只能有一个基本数据
    li = json.load(open("test", "r"))
    print(li, type(li))


def assert_ex():
    try:
        # there is e value in ''
        assert 1 == 0, 'One does not equal zero silly!'
    # AssertionError is not baseError
    except AssertionError, args:
        print '%s: %s' % (args.__class__.__name__, args)  # todo 参考类一章
        print '%s: %s' % (args.__class__.__doc__, args)
        # args （名字可以自己定义）是一个包含来自导致异常代码的诊断信息的类实例。
        # 类型：<class 'exception.TypeError'>
        #


def safe_float_raise(obj):
    excs = [ValueError, TypeError]
    ex_value = ValueError
    try:
        if str(obj) != '0':
            # select one from four is ok
            # raise TypeError
            # raise excs[0]
            # raise ValueError()
            # raise ex_value

            # select one from four is ok .there are is except with args
            # raise TypeError , 'type'
            # raise excs[0], 'type'
            # raise ValueError('type')
            # raise ex_value, 'type'

            # raise
            raise SomeCustomException("Bad hostname")
            # raise exceptionName，exceptArgs，exceptionTraceback
            # 三个参数分别是异常的名字、说明、跟踪记录对象（当重新引发异常时，可以区分先前和当前的位置）
            # raise exceptionName，exceptArgs 等同于 raise exceptionName(exceptArgs)
            # raise 不带任何参数，表示重新引发前一个异常，如果之前没有异常，出发typeError
            #TODO 异常列表
        else:
            return_val = float(obj)
    except (ValueError, TypeError), e:
         return_val = str(e)
    # baseError capture all except
    # - BaseException
    #   |- KeyboardInterrupt
    #   |- SystemExit
    #   |- Exception
    #      |- all other current built-in exception
    except BaseException, e:
        if type(e) == SomeCustomException:
            print e.args
        return_val = str(e)
    # no except
    else:
         print 'succeed'
    finally:
        return return_val


def more_error_information():
    try:
        float('abc123')
    except BaseException:
        import sys
        exc_tuple = sys.exc_info()
        print exc_tuple


class SomeCustomException(Exception):
    def __init__(self, arg):
        self.args = arg

#todo 如何查看变量的类型？
def safe_float_continuous_error(obj):
    try:
        return_val = float(obj)
    except (ValueError, TypeError), e:
        return_val = str(e)
    # baseError capture all except
    except baseError, e:
        return_val = str(e)
    # no except
    else:
        print 'succeed'
    finally:
        return return_val


def fun_with():
    """
    将open(r'somefileName')赋值给somefile
    无论接下来with段中出现什么情况，都会对当前对象进行清理工作。例如file的file.close()方法。
    系统自动创建一个上下文管理器，这个管理器就是在对象内实现了两个方法：__enter__() 和__exit__()
　　__enter__()方法会在with的代码块执行之前执行，__exit__（）会在代码块执行结束后执行。
　　__exit__()方法内会自带当前对象的清理方法。
    :return:
    """
    with open(r'somefileName') as somefile:
            for line in somefile:
                print line
    """
    nested 函数：
    with nested(A(), B(), C()) as (X, Y, Z):
         # with-body code here
    等同于：
    with A() as X:
        with B() as Y:
            with C() as Z:
                 # with-body code here
    """

def fun(x=5):
    def funcy(y):  # 内部的函数包含外部相关的参数（x）叫做内包。
        print (x, y)  # 内嵌函数定义结束
    return funcy  # 调用内嵌函数


def fun_args(inner_args):
    args = 2
    print ('locals', locals())  # 当前函数的局部变量
    # ('locals', {'args': 2, 'inner_args': 1})
    global QJBL
    QJBL = '全局变量'
    print ('globals', globals())
    """  全局变量
    ('globals', 
    {'fun_args': <function fun_args at 0x0000000004A6BAC8>, 
    'fun_print1': <function fun_print1 at 0x0000000004A6BB38>, 
    '__builtins__': <module '__builtin__' (built-in)>, 
    '__file__': 'C:/Users/fengjiexyb/Desktop/test.py', 
    '__package__': None, 
    'out_args': 'sss', 
    'fun_print': <function fun_print at 0x0000000004A6BBA8>, 
    'fun': <function fun at 0x0000000004A6BA58>, 
    '__name__': '__main__', 
    'main': <function main at 0x0000000004A6BC18>, 
    '__doc__': '\n@created time:2018/3/11 22:08\n@Python version: python 2.7.13(anaconda2 4.4.0 64-bit)
    \n@contact:QQ:120405752,xuyongbingwork@126.com\n@author: fengjiexyb\n@license: Apache Licence 
    \n@site: http://blog.csdn.net/fengjiexyb , https://github.com/fengjiexyb\n@software: PyCharm Community Edition
    \n@file: test.py\n@content:\n'})
    """


def fun_print1(fun_name):  # fun_name是一个函数，在python中函数也是一种对象，所以可以当做参数来传递。
    def print_name():
        print fun_name.__name__
    return print_name  # 没有括号，直接返回print_name函数。被主函数执行（实际是被调用fun_name的函数执行），所以只打印函数名。


def fun_print2(fun_name):  # fun_name是一个函数，在python中函数也是一种对象，所以可以当做参数来传递。
    def print_name():
        print fun_name.__name__
        return fun_name  # 和fun_print1相比，在执行fun_name之后，返回了fun_name。但是没有任何对象接收这个函数，直接被抛弃，没有执行fun_name。
    return print_name


def fun_print3(fun_name):  # fun_name是一个函数，在python中函数也是一种对象，所以可以当做参数来传递。
    def print_name():
        print fun_name.__name__
        return fun_name()  # 和fun_print1相比，在执行fun_name之后，继续执行fun_name（有括号）。打印了__doc__，version。
    return print_name


def fun_print4(fun_name):  # fun_name是一个函数，在python中函数也是一种对象，所以可以当做参数来传递。
    def print_name():
        print fun_name.__name__
    return fun_name  # 如果返回的不是print_name，就不会执行print_name，直接执行fun_name。
    # 如果fun_name加括号，就会出现fun_print0的错误。


@fun_print1
def fun_zhuangshiqi():
    """
    装饰器，相当于fun_print(fun_zhuangshiqi)。可以有多个装饰器。有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
    比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
    """
    # 上面的注释就是fun_zhuangshiqi.__doc__的值
    print fun_zhuangshiqi.__doc__
    try:
        print fun_zhuangshiqi.version
    except:
        pass
    fun_zhuangshiqi.__doc__ = "new doc"  # 也可以重新定义
    fun_zhuangshiqi.version = "v0.2"  # 定义函数版本，支持数字类型。
    # fun.__doc__ 、fun.versiond等等都可以在函数外赋值和调用
    print fun_zhuangshiqi.__doc__
    print fun_zhuangshiqi.version
    # print fun.__name__


def zhuangshiqi():
    """
    全局变量和装饰器
    :return:
    """
    print ('main_globals', globals())
    fun(8)(9)
    f = fun(8)  # 调用fun函数，设置x的值为8，定义了funcy函数
    f(9)  # 因为闭包，所以funcy函数已经知道了x=8，f(9)定义了y=9；另一种方式是直接调用fun(8)(9)
    fun_args(1)
    print('------------------------------')
    fun_zhuangshiqi()


def change_long_fun(formal_args,*tuple_args,**dict_args):
    """
    可变长度的参数示例，调用方法在TODO
    三类参数都可以省略，但如果同时使用。字典参数一定要在元组参数之后。
    :param formal_args: 正常的参数
    :param tuple_args: 元组参数（接收所有不确定的参数（不含字典参数），调用时不确定的参数数量可以为0），所谓不确定，表示该参数找不到其他的接收者（形参）
    :param dict_args: 字典参数（接收所有不确定的字典参数（所谓字典参数，就是a='dict'，这种带等号的），调用时不确定的参数数量可以为0）
    :return:
    """
    print '-'*20
    print 'formal args:',formal_args
    for each_tuple_arg in tuple_args:
        print 'tuple_args:',each_tuple_arg
    for each_dict_arg in dict_args:
        print 'dict_args:',each_dict_arg

def call_change_long_fun():
    change_long_fun(1) # 没使用元组参数和字典参数
    change_long_fun(1,2,3)  # 没使用字典参数
    change_long_fun(1,a=2)  # 没使用元组参数
    change_long_fun(1,2,a=3)
    change_long_fun(1,*(2,3),**{'a':4,'b':5})
    a = (2,3)
    b = {'x':4}
    change_long_fun(1,'s',y=5,*a,**b)

    add = partial(change_long_fun,5) # 通过partial将5传入到change_long_fun函数中的tuple_args，相当于在change_long_fun的加强版
    add(1)


class TestClass(object):
    """
    this is a test class.类名首字母大写
    """
    version=0.1 # 类属性，如果是对象属性不需要在此声明
    def __init__(self):# init函数的默认返回值是一个对象，所以不要显示的返回任何值。
        pass

    def test_fun(self):
        """
        方法可选择添加三种装饰器：
        @staticmethod 静态方法。静态方法是不能访问实例变量和类变量的。这种方法不需要传递self
        @classmethod 类方法。类方法只能访问类变量，不能访问实例变量。这种方法不需要传递self，但一般都会写一个cls代表类。
        @@property 属性方法。属性方法的作用就是通过@property把一个方法变成一个静态属性。变成属性之后调用时不需要写括号。
        :return:
        """
        pass


class ChildClass(TestClass):
    __name = 'python'  # 私有字段
    def test_fun(self): # 覆盖方法。注意：如果重写__init__方法，在实例化时是不会调用父类的__init__方法，这一点与java不同。
        super(TestClass,self).test_fun() # 调用父类被覆盖的方法，第二个参数self是当前实例。


def print_arguments():
    print TestClass.__dict__
    print TestClass.__name__
    print TestClass.__doc__
    print TestClass.__bases__
    print TestClass.__module__

def test_class_fun():
    tc = TestClass()
    #tc.print_arguments()
    print dir(TestClass)  # 类的属性和方法、包括'__doc__',  '__module__'
    print dir(tc)

    print(TestClass.version)
    print(tc.version)
    tc.version=0.2 # 实例属性
    print(TestClass.version)
    print(tc.version)
    tc.fun = print_arguments  # 添加一个类外部的方法给实例属性，
    tc.fun()

    if(hasattr(tc, 'version')): # 判断tc是否存在version属性
        attr = getattr(tc,'version') # 获取属性
        setattr(tc,'version',attr+0.1) # 设置属性
        delattr(tc,'version') # 删除属性
    cc= ChildClass()
    try:
        print (cc.__name) # 不可访问私有属性
    except:
        print('expect')
        print (cc._ChildClass__name) # 访问私有属性的方法：对象._类__字段名

def regex():
    """
    默认贪婪匹配，如果要懒惰模式，使用？
    :return:
    """
    s = 'eee13758838334,13328312112,dfkjghkdfjg'
    tel = '(0?(13|14|15|17|18|19)[0-9]{9})'
    m = re.match(tel,s)
    '''match
    如果在起始位置不能匹配，返回None。这是与search的区别。
    属性：（以下属性和方法大部分也适用于其他方法）

    string: 匹配时使用的文本。
    re: 匹配时使用的Pattern对象。
    pos: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
    endpos: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
    lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
    lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
    方法：
    
    group([group1, …]): 
    获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
    groups([default]): 
    以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
    groupdict([default]): 
    返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
    start([group]): 
    返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
    end([group]): 
    返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
    span([group]): 
    返回(start(group), end(group))。
    expand(template): 
    将匹配到的分组代入template中然后返回。template中可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。\id与\g<id>是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符'0'，只能使用\g<1>0。
    '''
    if m is not None:
        # group（）找到所有的匹配的字符串，但不会全部返回。
        # 返回模式中第n个括号的匹配字符串，n表示group中的参数。默认参数值为0，表示返回完整的匹配（不是括号内容了）
        # 参数个数可以是多个，但不能大于模式中的括号数
        print m.group()
        print '-'*20
        # groups（） 返回模式中所有括号的匹配字符串，作为一个元组返回。
        print m.groups()
    else:
        print 'None'

    print '-'*10 ,'end','-'*10
    m = re.search(tel, s)
    if m is not None:
        print m.group()
        print '-' * 20
        print m.groups()
    else:
        print 'None'

    print '-' * 10, 'end', '-' * 10
    m = re.findall(tel, s)
    print m

    print '-' * 10, 'end', '-' * 10
    s = '1775kjdhfi1775jdgf'
    tel = '17'
    m = re.split(tel, s)
    print m

    print '-' * 10, 'end', '-' * 10
    for m in re.finditer(tel,s): # 返回迭代器
        print m.group()

    print '-' * 10, 'end', '-' * 10
    print re.sub(tel, '**', s)

def ET_parser(gz):
    """
    使用et方法来解析xml文件，还要继续看一下
    :param gz: xml文件名，
    :return:
    """
    import os,gzip,cStringIO
    import xml.etree.cElementTree as ET

    vs_cnt = 0
    str_s = ''
    file_io = cStringIO.StringIO()
    xm = gzip.open(gz,'rb')
    print("已读入：%s.\n解析中：" % (os.path.abspath(gz)))
    tree = ET.ElementTree(file=xm)
    root = tree.getroot()
    for elem in root[1][0].findall('object'):
            for v in elem.findall('v'):
                    file_io.write(root[1].attrib['id']+' '+elem.attrib['TimeStamp']+' '+elem.attrib['MmeCode']+' '+\
                    elem.attrib['id']+' '+ elem.attrib['MmeUeS1apId']+' '+ elem.attrib['MmeGroupId']+' '+ v.text+'\n')
            vs_cnt += 1
    str_s = file_io.getvalue().replace(' \n','\r\n').replace(' ',',').replace('T',' ').replace('NIL','')    #写入解析后内容
    xm.close()
    file_io.close()
    return (str_s,vs_cnt)

def json_parser():
    import json
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    jsonData = json.dumps(data)
    print jsonData
    print jsonData.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')) # 格式化输出

    text = json.loads(jsonData)
    print text

if __name__ == '__main__':
    # main()
    # fun_iffor('a')
    # TODO pickle marshal shelve
    # filename = raw_input('enter input filename:')  # raw_input 不接受换行符.注意：完整路径
    # file_oper(filename)
    # fun()
    # print ('main_globals', globals())
    # call_change_long_fun()
    regex()
