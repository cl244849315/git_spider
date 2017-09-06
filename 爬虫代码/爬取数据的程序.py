# -*- enconding:etf-8 -*-
import pymysql
import os
import time
import re
serveraddr="localhost"
user="root"
password="123456"
databaseName="test"
filename="./data/UNCL.csv"
#读取文件里面的内容插入数据库
def InsertDataFromFile(absolutePath,file_name):
	file_name = file_name.split('.')[0]
	file_list_name = absolutePath.split(sep)
	if(len(file_list_name)>2):#设置父目录名字
		parent_name = file_list_name[len(file_list_name)-2]
	else:
		parent_name = "default_root"#缺省的根目录名字
	file_object = open(absolutePath)
	try:
		all_the_text = file_object.read()
	finally:
		file_object.close()
	all_the_text = all_the_text.strip(',')
	#all_the_text = all_the_text.replace('[','(');
	#splitList = all_the_text.replace(']',')');
	all_the_text = all_the_text.lstrip('[')
	all_the_text = all_the_text.rstrip(']') 
	splitList = all_the_text.split('],[')
	totalList = []
	for item in  splitList:
		arr = item.split(',')#将一组数据变成数据
		if config.GaomuTrue == 1:
			arr.insert(0,'0')#插入id
			arr.insert(3,parent_name+'_'+file_name.split(config.keyWord)[0])#插入文件名字
			arr.append(arr[4])
			arr.remove(arr[4])
			#text = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(arr[2]))
			#print text
			#arr[2] = text
			#arr.remove(arr[2])
			#arr.insert(2,text);
			#print time.localtime(int(arr[2]))
			#print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(arr[2])))
			#print int(arr[2])
		else:
			arr.insert(0,'0')#插入id
			arr.insert(1,file_name)#插入文件名字
		#totalList.insert(len(totalList),arr);
		totalList.append(arr)
	try:  
		#sql_string = 'insert into '+tableName+ ' values (0,'+ file_name +',%s,%s,%s,%s,%s) '
		sql_string = 'insert into '+tableName+ ' values (%s,%s,%s,%s,%s,%s,%s) '
		# 执行sql语句
		cur.executemany(sql_string,totalList)
	    # 提交到数据库执行
		conn.commit()
	except MySQLdb.Error,msg:  
		print file_name+" insert data error"
	    # 发生错误时回滚
		conn.rollback()
		return 0
	#cur.close()
	#conn.close()
	return len(totalList)#返回文件插入的条数

amountOfInsert = 0#统计本次插入的总数
def create_table():
	# sep=os.sep
	# tableName=raw_input('please input the table name which will be created:')
	# classpath=raw_input('请输入需要遍历的路径：')

	db=pymysql.connect(serveraddr,user,password,databaseName)
	cursor=db.cursor()
	cursor.execute("drop table if exists `tncl`")
	sql="""	create table `tncl`(
			`tncl_id` varchar(25) not null,
			`tncl_tag` varchar(25) not null,
			`tncl_desc` varchar(255) not null,
			`tncl_note` varchar(1200) not null,
			primary key(`tncl_id`)
			) engine=InnoDB default charset=utf8;"""
			
	cursor.execute(sql)
	db.close()
def test():
	p1=r"^\s{13}\w.+|\n$"
	pattern=re.compile(p1)
	fr=open(filename)
	w2=open('./data/e1.csv','a')
	for line in fr.readlines():
		print(line)
		matcher=re.findall(pattern,line)
		print(matcher)
		# print(type(matcher)) list
		for i in matcher:
			# print(i) 
			# print(type(i)) str
			for k in i:
				# print(k)
				# print(type(k)) str
				w2.write(k)
			# w2.write("\n")
		print("-----------")
	fr.close()
	w2.close()

	
if __name__=='__main__':
	test()