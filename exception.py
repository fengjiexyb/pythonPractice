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
        print '%s: %s' % (args.__class__.__name__, args)


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
            #raise ex_value, 'type'

            # raise
            raise SomeCustomException("Bad hostname")
        else:
            return_val = float(obj)
    except (ValueError, TypeError), e:
         return_val = str(e)
    # baseError capture all except
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


def main():
    print safe_float_raise('value')
    # assert_ex()
    # print safe_float_continuous_error('0.12')
    # print safe_float_continuous_error('value')
    # print safe_float_continuous_error({1, 2})


if __name__ == '__main__':
    main()
