# -*- coding:utf-8 -*-
import re
import os


import SetYear as sy


'''
适应旧版本
'''


year=sy.year#用户自定义
ss="./data/%s/TRSD/"%year#根目录
filename = ss+'TRSD%s.txt'%year#输入文件名




def trsd_nonote():
    try:
        os.rename(ss+'TRSD.%s'%year,ss+'TRSD%s.txt'%year)
    except:
        pass


    p1 = r"^\s{4}(?:X|\W)\s([A-Z]{3})\s{4}.+\n"#TCC
    p2 = r"\s{4}(?:X|\W)\s[A-Z]{3}\s{4}(.+)\n"
    """
           Function: To specify information regarding the transport
                     such as mode of transport, means of transport,
                     its conveyance reference number and the
                     identification of the means of transport.
    """
    p3 = r"^\s{6}Function:\s(.+\w\w\.)\n"
    p4 = r"^\s{6}Function:\s(.+\.g\.|.+[^\.])\n"
    # p4 = r"^\s{7}Function:\s(.+[\.g\.|[^\.]])\n"
    p5 = r"^\s{16}(\w.+[^\.])\n"
    p6 = r"^\s{16}(.+\.)\n"

    #Note
    # p7 = r"^\s{7}Note:\s\n"#Note
    # p8= r"^\s{12}([A-Z].+\.)\n"#Note内容只有1行
    # p9 = r"^\s{12}(.+[^\.]|)\n"#Note内容只多行的非最后行
    # p10 = r"^\s{12}(.+\.)\n"#Note内容只多行的最后行

    pattern1 = re.compile(p1)
    pattern2 = re.compile(p2)
    pattern3 = re.compile(p3)
    pattern4 = re.compile(p4)
    pattern5 = re.compile(p5)
    pattern6 = re.compile(p6)
    fr = open(filename)
    # temp = "";
    flag = 0
    for line in fr.readlines():
        matcher1 = re.findall(pattern1,line)
        matcher2 = re.findall(pattern2,line)
        matcher3 = re.findall(pattern3,line)
        matcher4 = re.findall(pattern4,line)
        matcher5 = re.findall(pattern5,line)
        matcher6 = re.findall(pattern6,line)
        #print matcher
        w2 = open(ss+'trsd_nonote%s.txt'%year,'a')#a代表追加 w代表重写
        if matcher1:
            flag = 1
            w2.write("\n")
            for j in matcher1:
                # for k in j:
                    w2.write(j)
        if ((matcher2!=[])and(flag ==1)):
            flag = 2
            w2.write(",")
            for j in matcher2:
                # for k in j:
                    w2.write(j)
        if ((matcher3!=[])and(flag ==2)):
            flag = 3
            #防止有逗号，用双引号括起
            w2.write(",\"")
            for j in matcher3:
                # for k in j:
                    w2.write(j)
            w2.write("\"")
        if ((matcher4!=[])and(flag ==2)):
            flag = 4
            w2.write(",\"")
            for j in matcher4:
                # for k in j:
                    w2.write(j)
        if ((matcher5!=[])and(flag ==4 or 5)):
            flag = 5
            w2.write(" ")
            for j in matcher5:
                # for k in j:
                    w2.write(j)
            # w2.write("\"")
        if ((matcher6!=[])and(flag ==4 or flag==5)):
            flag = 6
            w2.write(" ")
            for j in matcher6:
                # for k in j:
                    w2.write(j)
            w2.write("\"")
    w2.close( )

def trsd_note():

    p1 = r"^\s{4}(?:X|\W)\s[A-Z]{3}\s{4}.+\n"#匹配ADR
    p2 = r"^\s{10}Note:\s([^ ].+)\n"#Note
    p3= r"^\s{16}([^ ].+)\n"#Note内容
    p4= r"^\W+\n"
    pattern1 = re.compile(p1)
    pattern2 = re.compile(p2)
    pattern3 = re.compile(p3)
    pattern4 = re.compile(p4)


    fr = open(filename,'r',encoding='cp852')
    w2 = open(ss+'trsd_note%s.txt'%year,'a',encoding='utf-8')#a代表追加 w代表重写
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
            for j in matcher2:
                
                w2.write(j)
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
                # print(matcher4[0])
    w2.write("\n")
    w2.close( )
    fr.close()

def join():



    f1= open(ss+'trsd_note%s.txt'%year)
    f2 =open(ss+'trsd_nonote%s.txt'%year) 

    list_note=[]
    for line1 in f1:
        # print(line1)
        if line1.isspace():
            list_note.append('')
        else:
            list_note.append(line1)
         
    f1.close()

    # print(list_note)
    f2_w= open(ss+'trsd%s.csv'%year,'a')  
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
    trsd_nonote()
    trsd_note()
    join()
