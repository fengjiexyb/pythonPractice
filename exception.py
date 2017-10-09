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
@content: except
"""


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
    print safe_float_continuous_error('0.12')
    print safe_float_continuous_error('value')
    print safe_float_continuous_error({1, 2})


if __name__ == '__main__':
    main()
