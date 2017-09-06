# -*- coding:utf-8 -*-
import os
import re
p1=r"([0-9][0-9][AB])\.\w{3}$"

p2=r"^.+\,(\d{4}).+"

pattern1=re.compile(p1)
pattern2=re.compile(p2)
def get_dir(zz):
	listdir=[]
	for filename in os.listdir('./%s'%zz):
		listdir.append(filename)
		# print(filename)
		# print(type(filename))
	# print(listdir)
	return listdir

def joint_b0(listdir,zz):
	if not os.path.exists('./new/'):
		os.makedirs('./new/')
	fw=open('./new/%s.csv'%(zz),'a')
	# fff=open('./new/b4_0065.txt')
	for i in listdir:
		# print(i)
		j=40000
		matcher1=re.findall(pattern1,i)
		fr=open('./%s/%s'%(zz,i))
		for line in fr.readlines():
			try:
				# print(len(line))
				if(len(line)==40000):
					continue
				else:
					fw.write(matcher1[0]+'_%s'%j+','+line.strip('\n')+'\n')
					j=j+1
			except:
				pass
	fr.close()
	fw.close()	

def joint_b1(listdir,zz):#单独拼接
	if not os.path.exists('./new/'):
		os.makedirs('./new/')
	fw=open('./new/%s.csv'%(zz),'a')
	for i in listdir:
		# print(i)
		j=1
		matcher1=re.findall(pattern1,i)
		fr=open('./%s/%s'%(zz,i))
		for line in fr.readlines():

			# print(len(line))
			if(len(line)==4):
				continue
			else:
				fw.write(line)
				# pass

				

	fr.close()
	fw.close()


def sort_joint():
	# dir_list=['b0'],'b3','b4','b2_idsd','b3_idcd'


	dir_list=['stock']#用于编号和拼接，会在new目录下生成编号号码的文件
	for i in range(len(dir_list)):
		listdir=get_dir(dir_list[i])
		# print(listdir)
		joint_b0(listdir,dir_list[i])

def joint_only():
	dir_list=['stock']#用于拼接，将需要拼接的放到stock目录下，会在new目录下生成stock文件，然后根据需要修改名称
	for i in range(len(dir_list)):
		listdir=get_dir(dir_list[i])
		# print(listdir)
		joint_b1(listdir,dir_list[i])

def updata(zz):
	fr=open('./new/%s'%(zz))
	fw=open('./new/new.csv','a')
	for line in fr.readlines():
		matcher2=re.findall(pattern2,line)
		if(matcher2):
			fw.write(matcher2[0]+','+line)
			
def another_save():
	year_list=['00A','00B','01A','01B','01C',
	'02A','02B','03A','03B','04A','04B','05A','05B',
	'06A','06B','07A','07B','08A','08B','09A','09B',
	'10A','10B','11A','11B','12A','12B','13A','13B',
	'14A','14B','15A','15B','16A','16B','17A']
	# p1=r""
	fr=open("./new/b4/b4_0065.txt")
	fw=open("./new/b4/b4_new.csv",'a')
	for i in range(len(year_list)):
		j=40001
		for line in fr.readlines():
			# print(type(line))
			str1=line.strip('\n').split(',')
			# print(str1)
			# print(type)
			fw.write("%s_%s,%s,%s,%s\n"%(year_list[i],j,str1[0],str1[1],year_list[i]))
			j=j+1
		fr.seek(0)
if __name__=="__main__":
	# sort_joint()
	# joint_only()
	# updata('b4.csv')
	another_save()


