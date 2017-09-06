# -*- coding:utf-8 -*-
'''
从11c开始提取
'''
import re
import numpy as np
import os
year = '17A'
ss="./data/edmd/"
# filename=ss+"/EDMDI1.17A"
def get_tag():
    try:
        os.rename(ss+"/EDMDI1.17A",ss+"/EDMDI1.txt")
    except:
        pass
    f1=open(ss+"/EDMDI1.txt")
    p1=re.compile(r"^(?:\s{3}|X\s{2}|\W\s{2})([A-Z]{6})\s.+\n")
    list_tag=list()
    for line in f1.readlines():
        # print(line)
        match1=re.findall(p1,line)
        # print(match1)
        if match1:
            for j in match1:
                list_tag.append(j)
    # filename_w1= ss+'%s'%list_tag[MM]
    print(list_tag)
    return list_tag
def trmd_b1_nonote(list_tag):
    if not os.path.exists('./data/edmd/new/'):
        os.makedirs('./data/edmd/new/')

    for MM in range(len(list_tag)):
        try:
            os.rename(ss+'%s_D.17A'%list_tag[MM],ss+'%s.txt'%list_tag[MM])
        except:
            break

        filename_w= ss+'new/%s_w.txt'%list_tag[MM]
        if os.path.exists(filename_w):
            os.remove(filename_w)
        # import os

        # os.rename('./data/CODECO_D.02A','./data/CODECO_D.txt')
        filename_r = ss+'%s.txt'%list_tag[MM]  # txt文件和当前脚本在同一目录下，所以不用写具体路径
        #00010   UNH Message header      M   1
        pattern1   =  re.compile(r"(^\d{4,5})\s{3}[A-Z]{3}.+[CM]\s{3}\d*\s{1,}\|{0,}\n")#00010
        pattern1_2 =  re.compile(r"^\d{4,5}\s{3}([A-Z]{3}).+[CM]\s{3}\d*\s{1,}\|{0,}\n")#UNH
        #pattern1_3 =  re.compile(r"^\d{5}\s{3}[A-Z]{3}(.+)[CM]\s{3}\d*\s{1,}\|{0,}\n")#Message header
        pattern1_4 =  re.compile(r"^\d{4,5}\s{3}[A-Z]{3}.+([CM])\s{3}\d*\s{1,}\|{0,}\n")#C
        pattern1_5 =  re.compile(r"^\d{4,5}\s{3}[A-Z]{3}.+[CM]\s{3}(\d*)\s{1,}\|{0,}\n")#1
        #pattern2 = re.compile(r"^\d{5}.+Segment\sgroup\s(\d)*.+[CM]\s{3}\d*\-+\+\n" )#+结尾
        #00050       ---- Segment group 1  ------------------ C   9----------------+
        pattern4_1 = re.compile(r"(^\d{4,5}).+Segment\sgroup\s\d*.+[CM]\s{3}\d*.+\n")
        pattern4_2 = re.compile(r"^\d{4,5}.+Segment\sgroup\s(\d*).+[CM]\s{3}\d*.+\n")
        pattern4_3 = re.compile(r"^\d{4,5}.+Segment\sgroup\s\d*.+([CM])\s{3}\d*.+\n")
        pattern4_4 = re.compile(r"^\d{4,5}.+Segment\sgroup\s\d*.+[CM]\s{3}(\d*).+\n")
        #匹配每组的单独结尾的一行即没有Segment group的以+、+|、+||、+|||……结尾的的每个字段
        #如00280   RNG Range details                            C   1---------------+|
        pattern5_1 = re.compile(r"(^\d{4,5})\s{3}[A-Z]{3}.+[CM]\s{3}\d*\-+\+{1,10}\|{0,20}\n" )
        pattern5_2 = re.compile(r"^\d{4,5}\s{3}([A-Z]{3}).+[CM]\s{3}\d*\-+\+{1,10}\|{0,20}\n" )
        pattern5_3 = re.compile(r"^\d{4,5}\s{3}[A-Z]{3}.+([CM])\s{3}\d*\-+\+{1,10}\|{0,20}\n" )
        pattern5_4 = re.compile(r"^\d{4,5}\s{3}[A-Z]{3}.+[CM]\s{3}(\d*)\-+\+{1,10}\|{0,20}\n" )
        #以下是确定层级关系
        #匹配每组的单独结尾的一行即没有Segment group的以+、+|、+||、+|||……结尾的
        pattern5 = re.compile(r"^\d{5}\s{3}[A-Z]{3}.+[CM]\s{3}\d*\-+\+\|{0,10}\n" )
        #匹配每组的开头一行即有Segment group的以+、+|、+||、+|||……结尾的
        pattern2_1 = re.compile(r"^\d{5}.+Segment\sgroup\s(\d*).+[CM]\s{3}\d*\-+\+\n" )#+结尾
        pattern2_2 = re.compile(r"^\d{5}.+Segment\sgroup\s(\d*).+[CM]\s{3}\d*\-+\+\|\n" )#+|结尾
        pattern2_3 = re.compile(r"^\d{5}.+Segment\sgroup\s(\d*).+[CM]\s{3}\d*\-+\+\|\|\n" )#+||结尾
        pattern2_4 = re.compile(r"^\d{5}.+Segment\sgroup\s(\d*).+[CM]\s{3}\d*\-+\+\|\|\|\n" )
        pattern2_5 = re.compile(r"^\d{5}.+Segment\sgroup\s(\d*).+[CM]\s{3}\d*\-+\+\|\|\|\|\n" )
        pattern2_6 = re.compile(r"^\d{5}.+Segment\sgroup\s(\d*).+[CM]\s{3}\d*\-+\+\|\|\|\|\|\n" )
        pattern2_7 = re.compile(r"^\d{5}.+Segment\sgroup\s(\d*).+[CM]\s{3}\d*\-+\+\|\|\|\|\|\|\n" )
        #匹配有同时多个组同时结束的情况，即以++、++|、++||……++、++|、++||……等结尾的
        pattern3_1 = re.compile(r"^\d{5}.+[CM]\s{3}\d*\-+\+{2}\|{0,20}\n")# 匹配++、++|、++||……等结尾
        pattern3_2 = re.compile(r"^\d{5}.+[CM]\s{3}\d*\-+\+{3}\|{0,20}\n")# 匹配+++、+++|、+++||……等结尾
        pattern3_3 = re.compile(r"^\d{5}.+[CM]\s{3}\d*\-+\+{4}\|{0,20}\n")
        pattern3_4 = re.compile(r"^\d{5}.+[CM]\s{3}\d*\-+\+{5}\|{0,20}\n")
        pattern3_5 = re.compile(r"^\d{5}.+[CM]\s{3}\d*\-+\+{6}\|{0,20}\n")
        pattern3_6 = re.compile(r"^\d{5}.+[CM]\s{3}\d*\-+\+{7}\|{0,20}\n")


        flag = 0
        #listgr中第一个不为0的点
        pos = -1
        listgr =[0,0,0,0,0,0,0,0,0,0]

        fr = open(filename_r)
        w2 = open(filename_w,'a')#a代表追加 w代表重写
        # w2.write("code_pos,parent,TRSD_tag,year,list_tag[MM],S,R")
        for line in fr.readlines():
            matcher1 = re.findall(pattern1,line)
            matcher1_2 = re.findall(pattern1_2,line)
            #matcher1_3 = re.findall(pattern1_3,line)
            matcher1_4 = re.findall(pattern1_4,line)
            matcher1_5 = re.findall(pattern1_5,line)
            matcher2_1 = re.findall(pattern2_1,line)
            matcher2_2 = re.findall(pattern2_2,line)
            matcher2_3 = re.findall(pattern2_3,line)
            matcher2_4 = re.findall(pattern2_4,line)
            matcher2_5 = re.findall(pattern2_5,line)
            matcher2_6 = re.findall(pattern2_6,line)
            matcher2_7 = re.findall(pattern2_7,line)
            matcher3_1 = re.findall(pattern3_1,line)
            matcher3_2 = re.findall(pattern3_2,line)
            matcher3_3 = re.findall(pattern3_3,line)
            matcher3_4 = re.findall(pattern3_4,line)
            matcher3_5 = re.findall(pattern3_5,line)
            matcher3_6 = re.findall(pattern3_6,line)
            matcher4_1 = re.findall(pattern4_1,line)
            matcher4_2 = re.findall(pattern4_2,line)
            matcher4_3 = re.findall(pattern4_3,line)
            matcher4_4 = re.findall(pattern4_4,line)
            matcher5   = re.findall(pattern5,line)
            matcher5_1 = re.findall(pattern5_1,line)
            matcher5_2 = re.findall(pattern5_2,line)
            matcher5_3 = re.findall(pattern5_3,line)
            matcher5_4 = re.findall(pattern5_4,line)

            if matcher4_1!=[]:
                w2.write("\n")
                for j in matcher4_1:
                    for k in j:
                        w2.write(k)
            if matcher4_2!=[]:
                w2.write(",")
                #写入parent列
                if pos!= -1:
                    numgr =listgr[pos]
                else:
                    numgr = 0
                if numgr ==0:
                    w2.write("SG0,")
                else:
                    w2.write("SG"+str(numgr)+",")
                for j in matcher4_2:
                    for k in j:
                        w2.write("SG"+str(k))
            if matcher4_3!=[]:
                flag = 3
                w2.write(",")
                #默认写入year,list_tag[MM]两列
                w2.write(year+","+list_tag[MM]+",")
                for j in matcher4_3:
                    for k in j:
                        w2.write(k)
            if matcher4_4!=[]:
                w2.write(",")
                for j in matcher4_4:
                    for k in j:
                        w2.write(k)
            if matcher5_1!=[]:
                w2.write("\n")
                for j in matcher5_1:
                    for k in j:
                        w2.write(k)
            if matcher5_2!=[]:
                w2.write(",")
                #写入parent列
                if pos!= -1:
                    numgr =listgr[pos]
                else:
                    numgr = 0
                if numgr ==0:
                    w2.write("SG0,")
                else:
                    w2.write("SG"+str(numgr)+",")
                for j in matcher5_2:
                    for k in j:
                        w2.write(k)
            if matcher5_3!=[]:
                flag = 3
                w2.write(",")
                #默认写入year,list_tag[MM]两列
                w2.write(year+","+list_tag[MM]+",")
                for j in matcher5_3:
                    for k in j:
                        w2.write(k)
            if matcher5_4!=[]:
                w2.write(",")
                for j in matcher5_4:
                    for k in j:
                        w2.write(k)
            #确定层级关系，也就是确定listgr
            if(matcher5!=[]):
                for i in listgr:
                    if i==0:
                        pos = listgr.index(i)-1
                        break
                listgr[pos]=0
            if (matcher2_1!=[]):
                # print "2_1"
                for j in matcher2_1:
                    # print j
                    if(listgr[0]==0):
                        listgr[0]=j
                    else:
                        listgr[0]=0
                # print listgr
            if (matcher2_2!=[]):
                for j in matcher2_2:
                    #numgr_d = j
                    if(listgr[1]==0):
                        listgr[1]=j
                    else:
                        listgr[1]=0
            if (matcher2_3!=[]):
                for j in matcher2_3:
                    if(listgr[2]==0):
                        listgr[2]=j
                    else:
                        listgr[2]=0
            if (matcher2_4!=[]):
                for j in matcher2_4:
                    if(listgr[3]==0):
                        listgr[3]=j
                    else:
                        listgr[3]=0
            if (matcher2_5!=[]):
                for j in matcher2_5:
                    if(listgr[4]==0):
                        listgr[4]=j
                    else:
                        listgr[4]=0
            if (matcher2_6!=[]):
                for j in matcher2_6:
                    if(listgr[5]==0):
                        listgr[5]=j
                    else:
                        listgr[5]=0
            if (matcher2_7!=[]):
                for j in matcher2_7:
                    if(listgr[6]==0):
                        listgr[6]=j
                    else:
                        listgr[6]=0
            if (matcher3_1!=[]):
                for i in listgr:
                    if i==0:
                        pos = listgr.index(i)-1
                        break
                listgr[pos]=0
                listgr[pos-1]=0
            if (matcher3_2!=[]):
                for i in listgr:
                    if i==0:
                        pos = listgr.index(i)-1
                        break
                for k in range((pos-2),(pos+1)):
                    listgr[k]=0
            if (matcher3_3!=[]):
                for i in listgr:
                    if i==0:
                        pos = listgr.index(i)-1
                        break
                for k in range((pos-3),(pos+1)):
                    listgr[k]=0
            if (matcher3_4!=[]):
                for i in listgr:
                    if i==0:
                        pos = listgr.index(i)-1
                        break
                for k in range(pos-4,pos+1):
                    listgr[k]=0
            if (matcher3_5!=[]):
                for i in listgr:
                    if i==0:
                        pos = listgr.index(i)-1
                        break
                for k in range(pos-5,pos+1):
                    listgr[k]=0
            if (matcher3_6!=[]):
                for i in listgr:
                    if i==0:
                        pos = listgr.index(i)-1
                        break
                for k in range(pos-6,pos+1):
                    listgr[k]=0
             #确定层级关系结束
            if (matcher1!=[]):
                flag = 1
                w2.write("\n")
                for j in matcher1:
                    for k in j:
                        w2.write(k)
            #print listgr
            #判断当前lit不为0的位置
            for i in listgr:
                if i==0:
                    pos = listgr.index(i)-1
                    break
            if matcher1_2!=[]:
                flag = 2
                w2.write(",")
                #写入parent列
                if pos!= -1:
                    numgr =listgr[pos]
                else:
                    numgr = 0
                if numgr ==0:
                    w2.write("SG0,")
                else:
                    w2.write("SG"+str(numgr)+",")
                for j in matcher1_2:
                    for k in j:
                        w2.write(k)
        #    if matcher1_3!=[]:
        #        flag = 3
        #        w2.write(",")
        #        for j in matcher1_3:
        #            for k in j:
        #                w2.write(k)
            if matcher1_4!=[]:
                flag = 4
                w2.write(",")
                #默认写入year,list_tag[MM]两列
                w2.write(year+","+list_tag[MM]+",")
                for j in matcher1_4:
                    for k in j:
                        w2.write(k)
            if ((matcher1_5!=[])and(flag ==4)):
                flag = 5
                w2.write(",")
                for j in matcher1_5:
                    for k in j:
                        w2.write(k)
        w2.close()
        fr.close()
def trmd_b1_note(list_tag):
    for MM in range(len(list_tag)):
        filename_r = ss+'%s.txt'%list_tag[MM]
        filename_w =  ss+'new/%s_wnote.txt'%list_tag[MM]
        if os.path.exists(filename_w):
            os.remove(filename_w)

        fr = open(filename_r)
        w2 = open(filename_w,'a')
        m=0
        for line in fr.readlines():
            list1 = [3,6,9,12,15,18,21,24,27,30]
            for i in range(10):
                k = list1[i]
                # print k
                pattern1 = re.compile(r"^(\d{4,5})\s{"+str(k)+"}[^ ].+\n")
                matcher1 = re.findall(pattern1,line)
                if matcher1!=[]:
                    flag = 1
                    m = k
                    # print m
                    w2.write("\"\n")
                    # for j in matcher1:
                    #     w2.write(j)
                    flag = 1
                    w2.write("\"")
                    break
            v = m+5
            #print v
            pattern2 = re.compile(r"^\s{"+str(v)+"}([^ ].+)\n")
            matcher2 = re.findall(pattern2,line)
            if (matcher2!=[]):
                for j in matcher2:
                    w2.write(j)
                w2.write(" ")
                #防止匹配到下面结构中的行
            pattern3 = re.compile(r"(:?4.3\s{4}Message\sstructure)|(:?Pos\s+Tag\sName\s+S\s+R)")
            matcher3 = re.findall(pattern3,line)
            if (matcher3!=[]):
                break
        w2.write("\"")
        w2.close( )
        #把第一行的“修改为note
        old_file=filename_w
        fopen=open(old_file,'r')
        w_str=""
        i =0
        for line in fopen:
            i =i+1
            if ((re.search("\"",line)) and (i ==1)):
                    line=re.sub('\"','code_pos,note',line)
                    w_str+=line
            else:
                    w_str+=line
        # print w_str
        wopen=open(old_file,'w')
        wopen.write(w_str)
        fopen.close()
        wopen.close()
def join(list_tag):
    for MM in range(len(list_tag)):
        f1 = open(ss+'new/%s_w.txt'%list_tag[MM])
        f2 = open(ss+'new/%s_wnote.txt'%list_tag[MM])


        list_note=[]
        for line1 in f1:
            # print(line1)

            list_note.append(line1)
             
        f1.close()

        # print(list_note)
        f2_w= open(ss+'new/b1%s.csv'%year,'a')  
        # for i in range(len(list_note)):
        j=0
            # f2_r = open(ss+'/new/%s_w.txt'%list_tag[MM])
        for line2 in f2:

            str11="%s,%s\n"%(list_note[j].strip('\n'),line2.strip('\n'))
            j=j+1
            # print(i)
            # print(str11)
            f2_w.write(str11)


         
        f2.close()
    f2_w.close()


  
if __name__ == '__main__':
    list_tag=get_tag()
    trmd_b1_nonote(list_tag)
    trmd_b1_note(list_tag)
    join(list_tag) 
