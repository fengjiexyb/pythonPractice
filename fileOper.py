# -*- coding: utf-8 -*-  
'''
@finish time:2017-09-30
@author��fengjiexyb 
Python file operation
'''
from PIL import Image
from pylab import *

'''�ļ�������ϰ'''
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
    # ���� ��strip()ɾ���س���
    # s.strip(rm)        ɾ��s�ַ����п�ͷ����β����λ�� rmɾ�����е��ַ�
    # s.lstrip(rm)       ɾ��s�ַ����п�ͷ����λ�� rmɾ�����е��ַ�
    # s.rstrip(rm)      ɾ��s�ַ����н�β����λ�� rmɾ�����е��ַ�
    #  ��rmΪ��ʱ��Ĭ��ɾ���հ׷�������'\n', '\r',  '\t',  ' ')
    data=[line.strip() for line in file_object.readlines()]
    # ��һ��ɾ����ÿ��ĩβ�Ļس���
    file_object.seek(0)#ָ�뷵���ļ�ͷ
    # ���ִ��������䣬print���Զ���ĩβ��һ�����з������Ի��ӡ�����س���
    for eachline in file_object:
        print eachline
    file_object.seek(0)
    # �������ַ�ʽ���Ӷ��ţ��;Ϳ�����print�����Զ���ӻس���
    for eachline in file_object:
        print eachline,
    file_object.close();

'''������ͼƬ�ϵ�3���㣬��ȡ��3���������'''
def pointpic():
    im = array(Image.open('C:/Users/fengjiexyb/Desktop/ttt/Lenna.png'))
    imshow(im)
    print 'Please click 3 points'
    x = ginput(3)
    print 'you clicked:', x
    show()

def main():
    filename=raw_input('enter input filename:')#raw_input �����ܻ��з�.ע�⣺����·��
    fileOper(filename)

if __name__ == '__main__':
    main()