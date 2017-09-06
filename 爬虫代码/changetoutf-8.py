import chardet
import os
# ANSI文件转UTF-8
import codecs
import os

def strJudgeCode(str):
    return chardet.detect(str)

def readFile(path):

    f = open(path, 'r',endoding='ANSI')
    filecontent = f.read()
    f.close()

    return filecontent

def WriteFile(str, path):
    try:
        f = open(path, 'w')
        f.write(str)
    finally:
        if f:
            f.close()

def converCode(path):
    file_con = readFile(path)
    result = strJudgeCode(file_con)
    #print(file_con)
    if result['encoding'] == 'utf-8':
        #os.remove(path)
        a_unicode = file_con.decode('utf-8')
        gb2312 = a_unicode.encode('gbk')    
        WriteFile(gb2312, path)

def listDirFile(dir):
    list = os.listdir(dir)
    for line in list:
        print(line)
        filepath = dir+line
        print(filepath)
        # if os.path.isdir(filepath):
        #     listDirFile(filepath)
        # else:
        #     print(line)
        converCode(filepath)            

if __name__ == '__main__':

    # listDirFile('./TRMD/')
 
    # 文件所在目录
    file_path =r"C:\\Users\\Lenovo\\Desktop\\数据库设计\\爬虫脚本\\TRMD\\test"
    files = os.listdir(file_path)
     
    for file in files:
        file_name = file_path + '\\' + file
        f = codecs.open(file_name, 'r','cp852')
        ff = f.read()
        file_object = codecs.open(file_path + '\\' + file, 'w', 'utf-8')
        file_object.write(ff)
