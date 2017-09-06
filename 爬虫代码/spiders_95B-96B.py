
import urllib
import urllib.request
import bs4
from bs4 import BeautifulSoup as bs
import re
import os 

year = '96B'
ss="./data/%s/"%year
'''
适应网页爬取95B-96B

'''
def b0_trmd():
	if not os.path.exists(ss):
		os.makedirs(ss)
	# os.makedirs(ss)
	p1=r"^([A-Z]{6})"

	url = "http://www.stylusstudio.com/edifact/D%s/messages.htm"%year
	resp = urllib.request.urlopen(url)
	data = resp.read().decode('UTF-8')
	soup = bs(data, 'html.parser')    
	segment11= soup.find_all('table')# ResultSet
	segment1=segment11[0].find_all('td')[1:]#表示第几个table，此时表示进去html网页中的第7个table,[1:],<class 'list'>
	# segment2= soup.find_all('table')
	# print(type(segment1))#
	f2=open(ss+'./trmd1%s.txt'%year,'a',encoding='utf-8')
	f3=open(ss+'./b0%s.txt'%year,'a',encoding='utf-8')
	f4=open(ss+'./trmd%s.txt'%year,'a',encoding='utf-8')
	pattern1=re.compile(p1)
	tag_list=[]
	for item in segment1:
			# print(item.string)#如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容。
			str1=item.get_text()
			# if str1.strip()=="":用于判断字符串是否含空格
			# 	break
			if item.string==None:
				# print("hhusssssssssssssssssssss")
				break
			matcher1=re.findall(pattern1,str1)
			if matcher1:
				
				f3.write(matcher1[0]+','+year+'\n')
				tag_list.append(matcher1[0])
				f4.write(matcher1[0]+',')
			else:
				f4.write(str1+'\n')


			# print(type(str1))
			# test1(str1)
			# print(str1)#以文本方式呈现

			# print(item.get_text())#获取具体标签内部内容
			# print([text for text in item.stripped_strings] )#以列表方式呈现

			# str2=str([text for text in item.stripped_strings])
			# #print(type(str1[0][0]))
			f2.writelines(str1+'\n')
	f2.close()
	return tag_list
def test1(code_tag):

	url = "http://www.stylusstudio.com/edifact/D%s/%s.htm"%(year,code_tag)
	resp=None
	while(resp==None):
		try:
			resp = urllib.request.urlopen(url)
		except:
			pass
	data = resp.read().decode('UTF-8')
	soup = bs(data, 'html.parser')    
	segment11= soup.find_all('table')
	segment1=segment11[7].find_all('tr')#表示第几个table，此时表示进去html网页中的第7个table

 
	f2=open(ss+'./text1%s%s.txt'%(year,code_tag),'a',encoding='cp852')
	for item in segment1:

			# #print(item)
			'''
			<tr class="FrameTreeFont"><td><span class="FrameDrawFont">│
			<span class="FrameHideFont">─</span>│<span class="FrameHideFont">─</span>├─</span>
			<a class="FrameItemFont" href="DAM_.htm" target="classFrame" title="Damage">DAM</a> 
			Damage</td><td align="right"><span class="FrameDetailFont"> ×1 
			</span></td><td><span class="FrameDetailFont">(M)</span></td></tr>
			'''
			str12=item.get_text()
			# #print(str12)#以文本方式呈现
			# #print(type(str12))
			'''
			│─│─├─DAM Damage ×1 (M)
			'''
			# #print(item.td.span.get_text())#获取具体标签内部内容
			# #print([text for text in item.stripped_strings] )#以列表方式呈现
			'''
			['│', '─', '│', '─', '├─', 'DAM', 'Damage', '×1', '(M)']
			'''
			'''
			soup.get_text("|")#u'\nI linked to |example.com|\n'进一步，通过strip去除掉文本每个位的头尾空白。

			soup.get_text("|", strip=True)#u'I linked to|example.com'
			'''
			str1=str([text for text in item.stripped_strings])
			# #print(type(str1[0][0]))
			f2.writelines(str12+'\n')

	f2.close()
def test2(code_tag):
	# p1=r"^(?:├─|└─)(.+)\n"
	p1=r"^\W{2}(\w.+)\n"#
	# p1=r"^\W{2}(Segment\sGroup\s\w.+)\n"#segement为第一层
	# p2=r"^(?:│─├─|│─└─)(.+)\n"
	p2=r"^\W{4}(\w.+)\n"
	# p3=r"^(?:│───├─|│───└─|│─│─├─|│─│─└─)(.+)\n"
	p3=r"^\W{6}(\w.+)\n"
	# p4=r"^(?:)(.+)\n"

	p4=r"^\W{8}(\w.+)\n"
	p5=r"^\W{10}(\w.+)\n"
	p6=r"^\W{12}(\w.+)\n"
	p7=r"^\W{14}(\w.+)\n"
	p8=r"^\W{16}(\w.+)\n"

	p9=r"Segment\sGroup\s(\d+)\s"
	# p10="Segment Group "



	pattern1=re.compile(p1)
	pattern2=re.compile(p2)
	pattern3=re.compile(p3)
	pattern4=re.compile(p4)

	pattern5=re.compile(p5)
	pattern6=re.compile(p6)
	pattern7=re.compile(p7)
	pattern8=re.compile(p8)
	pattern9=re.compile(p9) 
	# pattern10=re.compile(p10)

	f1=open(ss+'./text1%s%s.txt'%(year,code_tag),'r',encoding='cp852')
	f2=open(ss+'./text2%s%s.txt'%(year,code_tag),'a',encoding='utf-8')	
	# c=int()
	# d=int()
	listp=[0,0,0,0,0,0,0,0]#用于记录父节点
	for line in f1.readlines():

		matcher1=re.findall(pattern1,line)
		matcher2=re.findall(pattern2,line)
		matcher3=re.findall(pattern3,line)
		matcher4=re.findall(pattern4,line)

		matcher5=re.findall(pattern5,line)
		matcher6=re.findall(pattern6,line)
		matcher7=re.findall(pattern7,line)
		matcher8=re.findall(pattern8,line)
		matcher9=re.findall(pattern9,line)
		# #print(type(matcher1))

		if matcher1:

			a='SG'+str(listp[0])+' '+matcher1[0]+'\n'
			f2.write(a)
			if matcher9:
				listp[1]=matcher9[0]
		if matcher2:

			b='SG'+str(listp[1])+' '+matcher2[0]+'\n'
			f2.write(b)
			if matcher9:
				listp[2]=matcher9[0]
		if matcher3:

			c='SG'+str(listp[2])+' '+matcher3[0]+'\n'
			f2.write(c)
			#print(c)
			if matcher9:
				listp[3]=matcher9[0]
		if matcher4:
			d='SG'+str(listp[3])+' '+matcher4[0]+'\n'
			f2.write(d)
			#print(d)
			if matcher9:
				listp[4]=matcher9[0]
		if matcher5:
			e='SG'+str(listp[4])+' '+matcher5[0]+'\n'
			f2.write(e)
			#print(d)
			if matcher9:
				listp[5]=matcher9[0]
		if matcher6:
			f='SG'+str(listp[5])+' '+matcher6[0]+'\n'
			f2.write(f)
			#print(d)
			if matcher9:
				listp[6]=matcher9[0]
		if matcher7:
			g='SG'+str(listp[6])+' '+matcher7[0]+'\n'
			f2.write(g)
			#print(d)
			if matcher9:
				listp[7]=matcher9[0]
		if matcher8:
			h='SG'+str(listp[7])+' '+matcher8[0]+'\n'
			f2.write(h)
			#print(d)
			if matcher9:
				listp[8]=matcher9[0]
	f2.close()
	f1.close()
	f3=open(ss+'./text3%s%s.txt'%(year,code_tag),'w',encoding='utf-8')
	f4=open(ss+'./text2%s%s.txt'%(year,code_tag),'r',encoding='utf-8')
	for line1 in f4.readlines():
		#print(line1)
		# f3.write(line1.replace(" "," "))
		f3.write(line1.replace("Segment Group ","SG"))
	f4.close()
	f3.close()
def test3(code_tag):
	f5=open(ss+'./text4%s%s.txt'%(year,code_tag),'a',encoding='utf-8')
	f6=open(ss+'./text3%s%s.txt'%(year,code_tag),'r',encoding='utf-8')
	p10=r"^(\w+)\s(\w+).+×([0-9]|[0-9]{2}|[0-9]{3}|[0-9]{4}|[0-9]{5})\s\((\w)\)$"
	pattern10=re.compile(p10)
	i=0
	for line2 in f6.readlines():
		i=i+1
		matcher10=re.findall(pattern10,line2)
		# print(matcher10)
		# print(type(matcher10))
		if matcher10:
			f5.write(str(matcher10[0])+'\n')

	f5.close()
	f6.close()
	# print(i)
	return i
def test4(code_tag):
	url = "http://www.stylusstudio.com/edifact/D%s/%s.htm"%(year,code_tag)
	resp=None

	while(resp==None):
		try:
			resp = urllib.request.urlopen(url)
		except:
			pass
	data = resp.read().decode('UTF-8')
	soup = bs(data, 'html.parser')    
	segment11= soup.find_all('p')
	# segment1=segment11[1].find_all('p')#表示第几个table，此时表示进去html网页中的第7个table
	# #print(segment1)	
	f2=open(ss+'./text5%s%s.txt'%(year,code_tag),'a',encoding='utf-8')
	for item in segment11:
		str12=item.get_text()
		#print(str12)#以文本方式呈现
		#print(type(str12))
		'''
		│─│─├─DAM Damage ×1 (M)
		'''
		# #print(item.td.span.get_text())#获取具体标签内部内容
		#print([text for text in item.stripped_strings] )#以列表方式呈现
		'''
		['│', '─', '│', '─', '├─', 'DAM', 'Damage', '×1', '(M)']
		'''
		'''
		soup.get_text("|")#u'\nI linked to |example.com|\n'进一步，通过strip去除掉文本每个位的头尾空白。

		soup.get_text("|", strip=True)#u'I linked to|example.com'
		'''
		str1=str([text for text in item.stripped_strings])
		#print(type(str1[0][0]))
		f2.writelines(str12+'\n')

	f2.close()
 
	# f2=open('./text1.txt','a',encoding='cp852')
	# for item in segment1:	
def test5(code_tag,num):
	f7=open(ss+'./text6%s%s.txt'%(year,code_tag),'a',encoding='utf-8')
	f8=open(ss+'./text5%s%s.txt'%(year,code_tag),'r',encoding='utf-8')
	p1=r"(^A\sservice\ssegment.+\n)"
	# p2=r"((?:A\s\w|^Date|^This|^Document|^In\s|^Requirements\s|^Dimensions|^The|^If\s|^Through|^Instructions|^For|^An).+\n)"
	p2=r"(^(?!Information|Note|It\sis\srecommended\sthat\swhere|ID\sshould\sbe\sspecified|All\sother\ssegments|A\sgroup\sof\ssegments\sthat\scontains\sa\sline\sitem\sand\sits\srelated\sinformation.+should\sbe\sconsigned.).+\n)"
	pattern1=re.compile(p1)
	pattern2=re.compile(p2)
	# pattern3=re.compile(p3)
	# pattern4=re.compile(p4)
	flag=0
	i=num
	for line3 in f8.readlines():
		matcher1=re.findall(pattern1,line3)
		matcher2=re.findall(pattern2,line3)
		# matcher3=re.findall(pattern3,line3)
		# matcher4=re.findall(pattern4,line3)

		# #print(matcher10)
		if matcher1 and flag==0:
			f7.write(matcher1[0])
			flag=1
			i=i-1
			if i==0:
				break
			continue
		if (matcher2 and (flag==1 or flag==2)):
			f7.write(matcher2[0])
			flag=2
			i=i-1
			continue
	f7.close()
	f8.close()

def join(code_tag):


	f1 =open(ss+'text6%s%s.txt'%(year,code_tag),'r',encoding='utf-8') 
	f2= open(ss+'text4%s%s.txt'%(year,code_tag),'r',encoding='utf-8')


	list_note=[]
	for line1 in f1:
		list_note.append(line1)
	f1.close()
	p11=r"^.+\'(\w+)\'.+\'\w+\'.+\'\w+\'.+\'\w+\'.+\n"
	p12=r"^.+\'\w+\'.+\'(\w+)\'.+\'\w+\'.+\'\w+\'.+\n"
	p13=r"^.+\'\w+\'.+\'\w+\'.+\'(\w+)\'.+\'\w+\'.+\n"
	p14=r"^.+\'\w+\'.+\'\w+\'.+\'\w+\'.+\'(\w+)\'.+\n"
	# print(list_note)
	f2_w= open(ss+'b1%s%s.txt'%(year,code_tag),'a',encoding='utf-8')
	f3_w= open(ss+'b1%s.csv'%year,'a',encoding='utf-8')  
	# for i in range(len(list_note)):
	i=0
	pattern11=re.compile(p11)
	pattern12=re.compile(p12)	
	pattern13=re.compile(p13)
	pattern14=re.compile(p14)	    
	# f2_r = open(ss+'/new/%s_w.txt'%list_tag[i])
	pos=[
	
	'0010','0020','0030','0040','0050','0060','0070','0080','0090','0100','0110','0120','0130','0140','0150','0160','0170','0180','0190','0200',
	'0210','0220','0230','0240','0250','0260','0270','0280','0290','0300','0310','0320','0330','0340','0350','0360','0370','0380','0390','0400',
	'0410','0420','0430','0440','0450','0460','0470','0480','0490','0500','0510','0520','0530','0540','0550','0560','0570','0580','0590','0600',
	'0610','0620','0630','0640','0650','0660','0670','0680','0690','0700','0710','0720','0730','0740','0750','0760','0770','0780','0790','0800',
	'0810','0820','0830','0840','0850','0860','0870','0880','0890','0900','0910','0920','0930','0940','0950','0960','0970','0980','0990','1000',
	'1010','1020','1030','1040','1050','1060','1070','1080','1090','1100','1110','1120','1130','1140','1150','1160','1170','1180','1190','1200',
	'1210','1220','1230','1240','1250','1260','1270','1280','1290','1300','1310','1320','1330','1340','1350','1360','1370','1380','1390','1400',
	'1410','1420','1430','1440','1450','1460','1470','1480','1490','1500','1510','1520','1530','1540','1550','1560','1570','1580','1590','1600',
	'1610','1620','1630','1640','1650','1660','1670','1680','1690','1700','1710','1720','1730','1740','1750','1760','1770','1780','1790','1800',
	'1810','1820','1830','1840','1850','1860','1870','1880','1890','1900','1910','1920','1930','1940','1950','1960','1970','1980','1990','2000',
	'2010','2020','2030','2040','2050','2060','2070','2080','2090','2100','2110','2120','2130','2140','2150','2160','2170','2180','2190','2200',
	'2210','2220','2230','2240','2250','2260','2270','2280','2290','2300','2310','2320','2330','2340','2350','2360','2370','2380','2390','2400',
	'2410','2420','2430','2440','2450','2460','2470','2480','2490','2500','2510','2520','2530','2540','2550','2560','2570','2580','2590','2600',
	'2610','2620','2630','2640','2650','2660','2670','2680','2690','2700','2710','2720','2730','2740','2750','2760','2770','2780','2790','2800',
	'2810','2820','2830','2840','2850','2860','2870','2880','2890','2900','2910','2920','2930','2940','2950','2960','2970','2980','2990','3000',
	'3010','3020','3030','3040','3050','3060','3070','3080','3090','3100','3110','3120','3130','3140','3150','3160','3170','3180','3190','3200',
	'3210','3220','3230','3240','3250','3260','3270','3280','3290','3300','3310','3320','3330','3340','3350','3360','3370','3380','3390','3400',
	'3410','3420','3430','3440','3450','3460','3470','3480','3490','3500','3510','3520','3530','3540','3550','3560','3570','3580','3590','3600',
	'3610','3620','3630','3640','3650','3660','3670','3680','3690','3700','3710','3720','3730','3740','3750','3760','3770','3780','3790','3800',
	'3810','3820','3830','3840','3850'

	]
	for line2 in f2:
		matcher11=re.findall(pattern11,line2)
		matcher12=re.findall(pattern12,line2)
		matcher13=re.findall(pattern13,line2)
		matcher14=re.findall(pattern14,line2)
		# print(matcher11[0])
		# print(matcher12[0])
		# print(matcher13[0])
		# print(matcher14[0])
		# print(matcher11[0])
		# a=list(line2)
		# print(a)
		# b=str(a)
		# print(b)
		# print(line2.split(','))
		try:
			str11="%s,%s,%s,%s,%s,%s,%s,\"%s\"\n"%(pos[i],code_tag,matcher12[0],matcher11[0],year,matcher14[0],matcher13[0],list_note[i].strip('\n'))
		
			i=i+1
			# print(i)
			# print(str11)
			f2_w.write(str11)
			f3_w.write(str11)
		except:
			print("---error---")
			break

	f2_w.close() 
	f2.close()

def test():#用户爬取网页，保存到本地
	filename='./codeco.txt'
	url = "http://www.stylusstudio.com/edifact/D95B/CODECO.htm"
	resp = urllib.request.urlopen(url)
	data = resp.read().decode('UTF-8')
	# f1=open(filename,'w')
	# f1.write(data)
	# #print(type(data))
	# #print(data)
	f2=open('./text.txt','a')
	soup = bs(data, 'html.parser')    

	# sw=soup.find_all('table',border=0,width="100%")
	# #print(sw[0])
	segment1= soup.find_all('h4')

	segment2= soup.find_all('p')
	# #print(type(segment))
	#print(segment1)
	#print(segment2)
	nowplaying_list = [] 
	for item in segment1:
			#print(item)
			# #print(item.name)
			# #print(item.attrs)
			# #print(type(item))
			#print(item.get_text())
			#print([text for text in item.stripped_strings] )
			f2.writelines(str([text for text in item.stripped_strings])+'\n')    
	        # nowplaying_dict = {}        
	        # nowplaying_dict['id'] = item['a']       
	        # for tag_img_item in item.find_all('img'):            
	        #     nowplaying_dict['name'] = tag_img_item['alt']            
	        #     nowplaying_list.append(nowplaying_dict)
	# result= segment[0].find_all('h4')
	# #print(result)

	for item in segment2:

			#print(item)
			#print(item.get_text())
			f2.writelines(str([text for text in item.stripped_strings] )+'\n')  
	f2.close()
	# data={}
	# data['word']='Jecvay Notes'
	 
	# url_values=urllib.parse.urlencode(data)
	# url="http://www.baidu.com/s?"
	# full_url=url+url_values
	 
	# data=urllib.request.urlopen(full_url).read()
	# data=data.decode('UTF-8')
	# #print(data)
if __name__=='__main__':
	tag=b0_trmd()
	for i in range(len(tag)):
		test1(tag[i])
		test2(tag[i])
		num=test3(tag[i])
		test4(tag[i])
		test5(tag[i],num)
		join(tag[i])
		print("------%s-----ok"%i)
	# str1='APERAK'
	# join(str1)
