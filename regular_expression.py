# -*- coding: utf-8 -*-
# 如无特殊情况, 文件一律使用 UTF-8 编码,文件头部必须加入#-*-coding:utf-8-*-标识。
# '#'注释如果不顶行，前有两个空格，后有一个空格。
"""
@created time:2018/4/10 21:43
@Python version: python 2.7.13(anaconda2 4.4.0 64-bit)
@contact:QQ:120405752,xuyongbingwork@126.com
@author: fengjiexyb
@license: Apache Licence 
@site: http://blog.csdn.net/fengjiexyb , https://github.com/fengjiexyb
@software: PyCharm Community Edition
@file: regular_expression.py
@content:本程序实现以下功能：
1、控制台输入文件名，该文件保存大量字符串；
2、控制台输入正则表达式；
3、在第一步的文件中搜索匹配正则表达式的字符串，将所有结果保存在result.txt文件中。
本程序的目的：
1、学习Python语言，在一个独立文件中描述怕Python基本语法。
2、学习代码规范，尽量满足《Google开源项目风格指南》（http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/contents/）
和《PEP 8 -- Style Guide for Python Code》（https://legacy.python.org/dev/peps/pep-0008/）
"""
# 先写文档注释，接下来是import。
# improt 一般按以下顺序导入：标准库、第三方库、自定义模块。两部分之间有一个空行。
# 不要使用from cgi import *
# 文档注释和代码可以使用PyCharm模板，具体设置方式参考：https://www.cnblogs.com/jhao/p/6944383.html?utm_source=itdadao&utm_medium=referral
# PyCharm快捷键参考：https://blog.csdn.net/fengjiexyb/article/details/79901050
# PyCharm会检查代码规范，尽量将右侧滚动条上的提示全部修复好。

import re  # re表示正则表达式。

class FileOper(object):
    """
    文件操作练习
    Python OS 文件/目录方法 http://www.runoob.com/python/os-file-methods.html
    """

    list_file = []  # 文件名列表
    dir_path = ''  # 文件夹路径

    def __init__(self, dir_path):  # 后加一个空格
        self.dir_path = dir_path  # 等号两侧加一个空格

    def file_open(self, file_name, mode_str):
        """
        输入文件夹路径，返回文件夹内的所有文件。
        :return: None
        """
        """
                mode 选择文件打开的模式。
                r表示读取（要求文件必须存在），
                w表示写入（不存在则创建；存在则删除内容；因为会清空原有文件的内容，一定要慎用），
                a表示追加（如果文件不存在会自动创建），+表示读和写，b表示二进制
                buffering 选择缓冲区大小
                0 表示没有缓冲区
                n（大于0的整数）缓冲n行
                n（小于0）使用系统默认设置
                """
        file_name = self.dir_path + '\\' + file_name
        file = open(file_name, mode=mode_str, buffering=-1)  # 读取文件
        self.list_file.append(file_name)
        return file

    def file_read(self, file_name):
        """
                readlines 读取所有剩余的行，返回一个列表。如果设置参数（数字），则返回的字符大约有参数大小的字节。（可能会略大于参数，因为要凑齐缓冲区）
                readline 读取当前位置到下一个行结束符之前的所有字符，返回字符串。如果设置参数（数字），则返回长度为参数的字符串（即不是一个完整行）。
                read() 不建议使用
                write（）、writelines() 与之对应，没有writeline()函数。
         """
        """
        # s.strip(rm)        删除s字符串中开头、结尾处，位于 rm删除序列的字符
        # s.lstrip(rm)       删除s字符串中开头处，位于 rm删除序列的字符
        # s.rstrip(rm)      删除s字符串中结尾处，位于 rm删除序列的字符
        #  当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
        """
        files = os.listdir(self.dir_path)  # 查找文件夹内的所有文件的文件名
        for filename in files:
            if file_name==filename:
                file_open = self.file_open(file_name, 'rb')
                print(file_open.encoding)  # 文件编码
                data = [eachline.strip() for eachline in file_open.readlines()]  # 读取文件的内容，删除了每行末尾的回车符
                """
              如果不去除换行符，可以使用一下方式读取每一行数据。
              在Python2中，这种方式*可能*会打印两个回车（即两行之间有一个空行），解决办法是在eachline后加一个逗号。Python3中没有这个问题。
                for eachline in file_object:
                     print eachline
              """
                return data
        return

    def file_write(self, file_name, str):
        file_open = self.file_open(file_name, 'wb')
        file_object.seek(0)  # 指针返回文件头
        file_open.write(str)

    def file_closeing(self):
        for file_name in self.list_file:
            file_name.close()
            if file_name.closed :  # 文件是否关闭
                print(file_name.name,'is closed')
                list1.remove(file_name)  # 删除元素,如果有多个，只删除第一个
            else:
                print(file_name.name, 'close worng!')
        self.list_file.clear()  # 清空列表

class RegexStr(object):
    def __init__(self):
        pass

class RegexExample(FileOper, RegexStr):
    def __init__(self):
        filename = raw_input('please enter input string filename:')  # raw_input 不接受换行符.注意：完整路径  todo 未完成
        string_regex = raw_input('please enter input regex string:')

if __name__ == '__main__':
    # Python 程序从第一个没有空格，不是类，也不是方法的行开始执行。
    # 一般由判断__name__='__main__'开始。
    # 如果本程序是直接执行，__name__='__main__'，如果是被别的程序调用执行，__name__= 模块名（regular_expression）
    # 参考http://blog.csdn.net/fengjiexyb/article/details/77838027
    re = RegexExample()

else:
    print('__name__ is %s', __name__)

# TODO 静态方法
    # file = 'C:\\Users\\fengjiexyb\\Desktop\\1.txt'
    # file = open(file, mode="rb", buffering=-1)  # 读取文件
    # for eachline in file:
    #     print(eachline)
    #     print(eachline,)