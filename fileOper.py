# -*- coding: utf-8 -*-  
'''
@finish time:2017-09-30
@author: fengjiexyb
Python file operation
'''
from PIL import Image
from pylab import *

'''文件操作练习'''
def fileOper(filename):
    # r is read; w is write;a is add.+ is read and write;b is binary mode
    # file is must exist when used r mode .
    # file is deleted when used w mode
    # when used a mode if file is not exist system will create file
    #

    # buffering =0 not buffer
    # buffering=n is buffer size=n lines
    # buffering noe setted or buffering <0 is default system setting
    file_object = open (filename,mode="r",buffering=-1)
    #file_object = open (filename,'rb')
    # readlines read all residual lines  and fun will exist enter char.
    # 所以 用strip()删除回车符
    # s.strip(rm)        删除s字符串中开头、结尾处，位于 rm删除序列的字符
    # s.lstrip(rm)       删除s字符串中开头处，位于 rm删除序列的字符
    # s.rstrip(rm)      删除s字符串中结尾处，位于 rm删除序列的字符
    #  当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
    data=[line.strip() for line in file_object.readlines()]
    # 上一行删除了每行末尾的回车符
    file_object.seek(0)#指针返回文件头
    # 如果执行下面语句，print会自动在末尾加一个换行符，所以会打印两个回车。
    for eachline in file_object:
        print eachline
    file_object.seek(0)
    # 下面这种方式（加逗号）就就可以让print不在自动添加回车符
    for eachline in file_object:
        print eachline,
    file_object.close();

'''用来在图片上点3个点，获取这3个点的坐标'''
def pointpic():
    im = array(Image.open('C:/Users/fengjiexyb/Desktop/ttt/Lenna.png'))
    imshow(im)
    print 'Please click 3 points'
    x = ginput(3)
    print 'you clicked:', x
    show()

def main():
    filename=raw_input('enter input filename:')#raw_input 不接受换行符.注意：完整路径
    fileOper(filename)

if __name__ == '__main__':
    main()