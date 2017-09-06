# -*- coding:utf-8 -*-
import re
import os

import SetYear as sy


'''
适应旧版本
'''


year=sy.year#用户自定义
ss="./data/%s/EDCD/"%year#根目录
filename = ss+'EDCD%s.txt'%year#输入文件名




def trcd_nonote():
    try:
        os.rename(ss+'EDCD.%s'%year,ss+'EDCD%s.txt'%year)
    except:
        pass


    p1 = r"^\s{4}...(C\d\d\d)\s.+\n"#C002
    p2 = r"^\s{4}...C\d\d\d\s(.+)\n"
    p3 = r"^\s{4}.\s{2}Desc:\s(.+\.)\n"
    p4 = r"^\s{4}.\s{2}Desc:\s(.+[^\.])\n"
    p5 = r"^\s{13}(.+[^\.])\n"
    p6 = r"^\s{13}(.+\.)\n"
    pattern1 = re.compile(p1)
    pattern2 = re.compile(p2)
    pattern3 = re.compile(p3)
    pattern4 = re.compile(p4)
    pattern5 = re.compile(p5)
    pattern6 = re.compile(p6)
    fr = open(filename)
    temp = ();
    flag = 0
    for line in fr.readlines():
        matcher1 = re.findall(pattern1,line)
        matcher2 = re.findall(pattern2,line)
        matcher3 = re.findall(pattern3,line)
        matcher4 = re.findall(pattern4,line)
        matcher5 = re.findall(pattern5,line)
        matcher6 = re.findall(pattern6,line)
        #print matcher
        w2 = open(ss+'trcd_nonote%s.txt'%year,'a')#a代表追加 w代表重写
        if matcher1:
            flag = 1
            w2.write("\n")
            for j in matcher1:
                for k in j:
                    w2.write(k)
                #for k in g:
                    #w2.write(k)
            #continue;
        if ((matcher2!=[])and(flag ==1)):
            flag = 2
            #print type(tup1)
            #print tup1
            #flag = 2
            w2.write(",")
            for j in matcher2:
                for k in j:
                    w2.write(k)
        if ((matcher3!=[])and(flag ==2)):
            flag = 3
            w2.write(",\"")
            for j in matcher3:
                for k in j:
                    w2.write(k)
            w2.write("\"")
        if (matcher4!=[]):
            w2.write(",\"")
            for j in matcher4:
                for k in j:
                    w2.write(k)
            flag = 4
        if ((matcher5!=[])and(flag ==4)):
            flag = 5
            w2.write(" ")
            for j in matcher5:
                for k in j:
                    w2.write(k)
        if ((matcher6!=[])and(flag ==4 or 5)):
            flag = 6
            w2.write(" ")
            for j in matcher6:
                for k in j:
                    w2.write(k)
            w2.write("\"")
    w2.close( )

def trcd_note():

    p1 = r"^\s{4}...(C\d\d\d)\s.+\n"#C002
    p2 = r"^\s{4}.\s{2}Note:\s\n"#Note
    p3= r"^\s{13}([^ ].+)\n"#Note内容
    p4= r"^\W+\n"
    pattern1 = re.compile(p1)
    pattern2 = re.compile(p2)
    pattern3 = re.compile(p3)
    pattern4 = re.compile(p4)


    fr = open(filename,encoding='cp852')
    w2 = open(ss+'trcd_note%s.txt'%year,'a',encoding='utf-8')#a代表追加 w代表重写
    # temp = ();
    flag = 0
    flag1=0
    for line in fr.readlines():
        matcher1 = re.findall(pattern1,line)
        matcher2 = re.findall(pattern2,line)
        matcher3 = re.findall(pattern3,line)
        matcher4 = re.findall(pattern4,line)

       
        #print matcher

        if matcher1!=[]:
            flag = 1
            w2.write("\n")
            # for j in matcher1:
                
            #     w2.write(j)

        if ((matcher2!=[])and(flag == 1)):
            flag = 2
            flag1=1
            # w2.write(",")
        if flag1==1:
            if ((matcher3!=[])and(flag ==2 or 3)):
                flag = 3
                w2.write(" ")
                for j in matcher3:
                    
                    w2.write(j)
            # w2.write(")
            if ((matcher4!=[])and(flag == 3)):
                flag=0
                flag1=0
    w2.write("\n")
    w2.close( )
    fr.close()

def join():



    f1= open(ss+'trcd_note%s.txt'%year)
    f2 =open(ss+'trcd_nonote%s.txt'%year) 

    list_note=[]
    for line1 in f1:
        # print(line1)
        if line1.isspace():
            list_note.append('')
        else:
            list_note.append(line1)
         
    f1.close()

    # print(list_note)
    f2_w= open(ss+'trcd%s.csv'%year,'a')  
    # for i in range(len(list_note)):
    i=0
        # f2_r = open(ss+'/new/%s_w.txt'%list_tag[i])
    for line2 in f2:

        str11="%s,\"%s\"\n"%(line2.strip('\n'),list_note[i].strip('\n'))
        i=i+1
        # print(i)
        # print(str11)
        f2_w.write(str11)


    f2_w.close() 
    f2.close()
if __name__ == '__main__':
    trcd_nonote()
    trcd_note()
    join()
