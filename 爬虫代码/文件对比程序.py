#-*- encoding:utf-8 -*-

class loadDatas(object):
    def __init__(self):
        self.path='./data'
    def load_compare(self):
        l1={}
        f1=open(self.path+'/95b.txt',encoding='utf-8')
        l2={}
        f2=open(self.path+'/05b.txt',encoding='utf-8')
        f=open(self.path+'/1.txt','a')
        # w2=open('./data/1.txt','a')

            # flag=1
        str1=[]
        # print(type(str1))
        # int i
        for line2 in f2:
            print(line2)
            (tag2,name)=line2.strip().split("  ")
            flag=0
            for line1 in f1:
            # 读完一次循环后，line1已经到底了，第2次循环便不进入;
            # f1.readlines()只能进入一次，一次读取整个文件;
            
                (tag1,name)=line1.strip().split("  ")
                print(tag1)
                if tag2==tag1:
                    print("a")
                    flag=0
                    break
                else:
                    print('d')
                    flag=1
                    # break
            # print("aa")
            if flag==1:
                # print("aa")
                str1.append(line2)
            f1.seek(0)
        print(str1)
        f.writelines(str1)   

        f1.close()
        f2.close()
        f.close() 
  
if __name__=='__main__':
    ld=loadDatas()
    ld.load_compare()