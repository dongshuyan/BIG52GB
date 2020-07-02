from langconv import *
import os       
import sys 
import re
def simple2tradition(line):
    #将简体转换成繁体
    line = Converter('zh-hant').convert(line.decode('utf-8'))
    #line = line.encode('utf-8')
    return line
 
def tradition2simple(line):
    # 将繁体转换成简体
    line = Converter('zh-hans').convert(line.decode('utf-8'))
    #line = line.encode('utf-8')
    return line

def TraditionalToSimplified(line):          #繁体转简体
    line=Converter("zh-hans").convert(line)
    return line


def SimplifiedToTraditional(line):          #简体转繁体
    line=Converter("zh-hant").convert(line)
    return line




def BIG52GB(path):
    with open(path, 'r') as f1:
        list1 = f1.readlines()
    for i in range(len(list1)):
        list1[i]=TraditionalToSimplified(list1[i])
    newpath=''
    while not(path.find('.')==-1):
        newpath=newpath+"."+path[:path.find('.')]
        path=path[path.find('.')+1:]
    newpath=newpath[1:]+'.GB.'+path
    f=open(newpath,'w')
    for child in list1:
        f.write(child)
    f.close()

def BIG52GB_path(path):
    files = os.listdir(path)
    for file_ in files:
        if os.path.isfile(path+file_):
            if (file_.find('.ass') >=0 or file_.find('.srt') >=0 )and file_[0]!='.' :
                print("file=",file_)
                BIG52GB(path+file_)

if __name__ == '__main__':
    lan  = input("Please choose language: \n(中文请输入CN, EN for English.) \nExample:CN\n")
    if len(re.findall(r"CN",lan)) >0:
        path= input("请输入字幕文件所在文件夹绝对路径.\n例如: /Users/moyu/Downloads/subtitle\n")
    elif len(re.findall(r"EN",lan))>0:
        path= input("Please enter the absolute path of the folder where the subtitle file is located\n例如: /Users/moyu/Downloads/subtitle\n")
    else:
        print("Error, Thanks for using!")
        exit()
    if (path[len(path)-1]!='/'):
        path=path.strip()+"/"
    print("\n\n_____________START_____________")
    BIG52GB_path(path)


    '''
    path = sys.argv[1]
    if (path[len(path)-1]!='/'):
        path=path.strip()+"/"
    BIG52GB_path(path)
    '''

