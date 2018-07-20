# -*- coding: utf-8 -*-
"""
@finish time:2017/10/9 10:50
@Python version: python 2.7.13(anaconda2 4.4.0 64-bit)
@contact:QQ:120405752,xuyongbingwork@126.com
@author: fengjiexyb
@license: Apache Licence 
@site: http://blog.csdn.net/fengjiexyb , https://github.com/fengjiexyb
@software: PyCharm Community Edition
@file: exception.py
@content: except and assert
"""


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


def main():
    print safe_float_raise('value')
    # assert_ex()
    # print safe_float_continuous_error('0.12')
    # print safe_float_continuous_error('value')
    # print safe_float_continuous_error({1, 2})


if __name__ == '__main__':
    main()
