# -*- coding:utf-8 -*-
import re
import os

import SetYear as sy


'''
适应旧版本
'''


year=sy.year#用户自定义
ss="./data/%s/IDSD/"%year
filename = ss+'IDSD%s.txt'%year


'''
适应旧版本

'''
try:
    os.rename(ss+'IDSD.%s'%year,ss+'IDSD%s.txt'%year)
except:
    pass


p1 = r"^\s{4}(?:X|\W)\s([A-Z]{3})\s{3}.+\n"#TC
p2 = r"(^\d{3})\s{3}[A-Z]\d{3}.+[CM]\s+.+\n"#010
p3 = r"^\d{3}\s{3}([A-Z]\d{3}).+[CM]\s+.+\n"#C552
p4 = r"^\d{3}\s{3}[A-Z]\d{3}.+([CM])\s+.+\n"#M
# p5 = r"^\d{3}\s{3}C\d{3}.+[CM]\s+(\d)\n"#1
p6= r"(^\d{3})\s{3}\d{4}.+[CM]\s{2}.*(?:.*\.\.\d+|.*\d+)\n"#单独的030
p7 =r"^\d{3}\s{3}(\d{4}).+[CM]\s{2}(?:.*\.\.\d+|.*\d+)\n"#单独的3286
p8 =r"^\d{3}\s{3}\d{4}.+([CM])\s{2}(?:.*\.\.\d+|.*\d+)\n"#单独的M
# p9 =r"^\d{3}\s{3}\d{4}.+[CM]\s{2}.*\.\.\d+\n"#单独的1
p10 =r"^\d{3}\s{3}\d{4}.+[CM]\s{2}(?:(.*\.\.\d+)|(.*\d+))\n"#单独的an..35



pattern1 = re.compile(p1)
pattern2 = re.compile(p2)
pattern3 = re.compile(p3)
pattern4 = re.compile(p4)
# pattern5 = re.compile(p5)
pattern6 = re.compile(p6)
pattern7 = re.compile(p7)
pattern8 = re.compile(p8)
# pattern9 = re.compile(p9)
pattern10 = re.compile(p10)

fr = open(filename)
temp = ();
flag = 0
for line in fr.readlines():
    matcher1 = re.findall(pattern1,line)
    matcher2 = re.findall(pattern2,line)
    matcher3 = re.findall(pattern3,line)
    matcher4 = re.findall(pattern4,line)
    # matcher5 = re.findall(pattern5,line)
    matcher6 = re.findall(pattern6,line)
    matcher7 = re.findall(pattern7,line)
    matcher8 = re.findall(pattern8,line)
    # matcher9 = re.findall(pattern9,line)
    matcher10 = re.findall(pattern10,line)
    #print matcher
    w2 = open(ss+'b2_%s.csv'%year,'a')#a代表追加 w代表重写
    if (matcher1!=[]):
        for g in matcher1:
            flag = 1
            temp = g
    if ((matcher2!=[])and(flag ==1 or 2)):
        flag = 2
        w2.write("\n"+temp+",")
        for j in matcher2:
            for k in j:
                w2.write(k)
    if ((matcher3!=[])and(flag ==2)):
        flag = 3
        w2.write(",")
        for j in matcher3:
            for k in j:
                w2.write(k)
        #复合的缺省为0000
        w2.write(",0000")
    if ((matcher4!=[])and(flag ==3)):
        flag = 4
        w2.write(",")
        for j in matcher4:
            for k in j:
                w2.write(k)
        #增加固定列year
        w2.write(","+year+",")
    # if ((matcher5!=[])and(flag ==4)):
    #     flag = 5
    #     w2.write(",")
    #     for j in matcher5:
    #         for k in j:
    #             w2.write(k)
    #     w2.write(", ")
    # print len(matcher6)
    if(len(matcher6)==1 and matcher6!=[''] ):

        flag = 6
        w2.write("\n"+temp+",")
        for j in matcher6:
            for k in j:
                w2.write(k)
        #单独的缺省为C000
        w2.write(",C000")
    if ((matcher7!=[])and(flag ==6)):
        flag = 7
        w2.write(",")
        for j in matcher7:
            for k in j:
                w2.write(k)
    if ((matcher8!=[])and(flag ==7)):
        flag = 8
        w2.write(",")
        for j in matcher8:
            for k in j:
                w2.write(k)
        #增加固定列year
        w2.write(","+year)
    # if ((matcher9!=[])and(flag ==8)):
    #     flag = 9
    #     w2.write(",")
    #     for j in matcher9:
    #         for k in j:
    #             w2.write(k)
    if ((matcher10!=[])and(flag ==8)):
        flag = 10
        w2.write(",")
        for j in matcher10:
            for k in j:
                w2.write(k)
    w2.close( )

"""
特殊情况



"""