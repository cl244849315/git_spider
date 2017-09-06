# -*- coding:utf-8 -*-
import re
import os


'''


注意：
1）17A文件改完后缀后，需要转为UTF-8无BOM格式，才能正确处理。
2）fr = open(filename,encoding='utf-8')

'''

import SetYear as sy


'''
适应旧版本
'''


year=sy.year#用户自定义
ss="./data/%s/UNCL/"%year#根目录
version='1'
filename = ss+'UNCL-%s-%s.txt'%(version,year)#输入文件名



def tncl_note():
    try:
        os.rename(ss+'UNCL-%s.%s'%(version,year),ss+'UNCL-%s-%s.txt'%(version,year))
    except:
        pass


    # p4= r"^(?:\s{5}|X\s{4}|\W\s{4})(\w+)\s+\w.+\n"
    p1 = r"^.\s(\d\d\d\d)\s\s[A-Z].+\n"#匹配tncl_id
    p2 = r"^.\s+([0-9]*[A-Z]*[0-9]*)\s+\w.+\n"#匹配tncl_tag
    p3 = r"^.\s+[0-9]*[A-Z]*[0-9]*\s+(\w.+)\n"#匹配tncl_name
    p4 = r"^\s{13}([^ ].+)\n"#匹配tncl_desc和#Note内容


    p5 = r"^\s{11}Note:\s\n"#Note
    # p6=r""
 

    pattern1 = re.compile(p1)
    pattern2 = re.compile(p2)
    pattern3 = re.compile(p3)
    pattern4 = re.compile(p4)

    pattern5 = re.compile(p5)


    fr = open(filename,encoding='cp852')
    temp = str();
    flag = 0
    w2 = open(ss+'tncl-%s-%s.csv'%(version,year),'a',encoding='utf-8')#a代表追加 w代表重写
    flag1=0
    for line in fr.readlines():
        matcher1 = re.findall(pattern1,line)
        matcher2 = re.findall(pattern2,line)
        matcher3 = re.findall(pattern3,line)
        matcher4 = re.findall(pattern4,line)
        matcher5 = re.findall(pattern5,line)

        #print matcher
        # print(matcher2)
        if matcher1:
            for g in matcher1:
                flag = 1
                temp = g

            continue
        if ((matcher2!=[]) and(flag==1 or 4)and(temp!='')and(matcher4==[])):
            if(len(matcher2[0])!=0):
                flag = 2
                w2.write("\",\"\"\n"+temp+"_"+matcher2[0]+","+matcher2[0])
                # print(len(matcher2[0]))
                # for j in matcher2:
                #     for k in j:
                # w2.write(matcher2[0])
            # else:
            #     continue
        if matcher3 and flag==2:
            flag = 3
            w2.write(",\"")
            for j in matcher3:
                for k in j:
                    w2.write(k)
            w2.write("\",\"")
        if matcher4 and (flag==3 or flag==4):
            flag=4
            for j in matcher4:
                for k in j:
                    w2.write(k)
        
        if ((matcher5!=[])and(flag == 4)):
            # flag = 5
            w2.write("\",\"")
            # continue
            # flag1=1
  
    w2.write("\",\"\"\n")
    w2.close( )
def join():



    f1= open(ss+'tncl-%s-%s.csv'%(version,year))

    list_note=[]
    for line1 in f1:
        # print(line1)

        list_note.append(line1)
         
    f1.close()
    # print(list_note[1].split(','))
    # print("%s_%s,%s\n"%(list_note[1].split(',')[0],list_note[1].split(',')[1],list_note[1].strip('\n')))
    # list_note[i].strip('\n')
    # print(list_note)
    # f2_w1= open(ss+'tred%s.csv'%year,'a')  
    f2_w2= open(ss+'b4-%s-%s.csv'%(version,year),'a',encoding='utf-8')  
    # for i in range(len(list_note)):
    # i=0
    
    for i in range(1,len(list_note)):

        # str11="%s_%s,%s\n"%(list_note[i].split(',')[0],list_note[i].split(',')[1],list_note[i].strip('\n'))

        str12="%s,%s,%s\n"%(list_note[i].split(',')[0],list_note[i].split(',')[1],year)
        # f2_w1.write(str11)
        f2_w2.write(str12)


    # f2_w1.close() 
    f2_w2.close()
    # f2.close()

if __name__ == '__main__':

    tncl_note()
    join()