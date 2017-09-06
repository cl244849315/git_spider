# -*- coding:utf-8 -*-
import re
import os
import SetYear as sy


year=sy.year
ss="./data/%s/IDCD/"%year#根目录
filename = ss+'IDCD%s.txt'%year#输入文件名


'''
适应旧版本
'''     
try:
    os.rename(ss+'IDCD.%s'%year,ss+'IDCD%s.txt'%year)
except:
    pass

p1 = r"^\s{4}.\s\s(\w\d{3})\s.+\n"#匹配C002
p2 = r"^(\d\d\d).{4}\d{4}\s{2}.+[CM]\s+(?:.*\.\.\d+|.*)\n"#C      n3
p3 = r"^\d\d\d.{4}(\d{4})\s{2}.+[CM]\s+(?:.*\.\.\d+|.*)\n"
p4 = r"^\d\d\d.{4}\d{4}\s{2}.+([CM])\s+(?:.*\.\.\d+|.*)\n"
p5 = r"^\d\d\d.{4}\d{4}\s{2}.+[CM]\s+((?:.*\.\.\d+|.*))\n"

p6 = r"^(\d\d\d).{4}\d{4}\s{2}.+[^\d]$\n"
p7 = r"^\d\d\d.{4}(\d{4})\s{2}.+[^\d]$\n"
p8 = r"^\s{13}.+([CM])\s+(?:.*\.\.\d+|.*)\n"
p9 = r"^\s{13}.+[CM]\s+((?:.*\.\.\d+|.*))\n"
pattern1 = re.compile(p1)
pattern2 = re.compile(p2)
pattern3 = re.compile(p3)
pattern4 = re.compile(p4)
pattern5 = re.compile(p5)

pattern6 = re.compile(p6)
pattern7 = re.compile(p7)
pattern8 = re.compile(p8)
pattern9 = re.compile(p9)
fr = open(filename)
temp = "";
flag = 0
for line in fr.readlines():
    matcher1 = re.findall(pattern1,line)
    matcher2 = re.findall(pattern2,line)
    matcher3 = re.findall(pattern3,line)
    matcher4 = re.findall(pattern4,line)
    matcher5 = re.findall(pattern5,line)

    matcher6 = re.findall(pattern6,line)
    matcher7 = re.findall(pattern7,line)
    matcher8 = re.findall(pattern8,line)
    matcher9 = re.findall(pattern9,line)
    #print matcher
    w2 = open(ss+'b3_%s.csv'%year,'a')#a代表追加 w代表重写
    if matcher1:
        flag = 1
        for j in matcher1:
            temp = j
    if ((matcher2!=[])and(flag ==1 or 5 or 9)):
        flag = 2
        w2.write("\n"+temp+","+year+",")
        for j in matcher2:
            for k in j:
                w2.write(k)

    if ((matcher3!=[])and(flag ==2)):
        flag = 3
        w2.write(",")
        for j in matcher3:
            for k in j:
                w2.write(k)

    if ((matcher4!=[])and(flag ==3)):
        flag = 4
        w2.write(",")
        for j in matcher4:
            for k in j:
                w2.write(k)
        
    if ((matcher5!=[])and(flag ==4)):
        flag = 5
        w2.write(",")
        for j in matcher5:
            for k in j:
                w2.write(k)

    if ((matcher6!=[])and(flag ==1 or 5 or 9)):
        flag = 6
        w2.write("\n"+temp+",")
        for j in matcher6:
            for k in j:
                w2.write(k)
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
        
    if ((matcher9!=[])and(flag ==8)):
        flag = 9
        w2.write(",")
        for j in matcher9:
            for k in j:
                w2.write(k)
w2.close( )

