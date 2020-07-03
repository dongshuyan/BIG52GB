from langconv import *
import os       
import sys 
import re
def simple2tradition(line):
    #将简体转换成繁体
    line = Converter('zh-hant').convert(line.encode('utf-8').decode('utf-8'))
    line = line.encode('utf-8')
    return line
 
def tradition2simple(line):
    # 将繁体转换成简体
    line = Converter('zh-hans').convert(line.encode('utf-8').decode('utf-8'))
    line = line.encode('utf-8')
    return line

def TraditionalToSimplified(line):          #繁体转简体
    line=Converter("zh-hans").convert(line)
    return line


def SimplifiedToTraditional(line):          #简体转繁体
    line=Converter("zh-hant").convert(line)
    return line




def BIG52GB(path):
    pan=0
    try:
        with open(path, 'r') as f1:
            list1 = f1.readlines()
    except:
        pan=1
        with open(path, "r", encoding='UTF-8') as f1:
            list1 = f1.readlines()
    for i in range(len(list1)):
        list1[i]=TraditionalToSimplified(list1[i])
    newpath=''
    while not(path.find('.')==-1):
        newpath=newpath+"."+path[:path.find('.')]
        path=path[path.find('.')+1:]
    newpath=newpath[1:]+'.GB.'+path
    if pan==0:
        f=open(newpath,'w') 
    else:
        f=open(newpath,'wb') 
    for child in list1:
        if pan==0:
            f.write(child)
        else:
            f.write(child.encode('UTF-8'))
    f.close()

def GB2BIG5(path):
    pan=0
    try:
        with open(path, 'r') as f1:
            list1 = f1.readlines()
    except:
        pan=1
        with open(path, "r", encoding='UTF-8') as f1:
            list1 = f1.readlines()
    for i in range(len(list1)):
        list1[i]=SimplifiedToTraditional(list1[i])
    newpath=''
    while not(path.find('.')==-1):
        newpath=newpath+"."+path[:path.find('.')]
        path=path[path.find('.')+1:]
    newpath=newpath[1:]+'.BIG5.'+path
    if pan==0:
        f=open(newpath,'w') 
    else:
        f=open(newpath,'wb') 
    for child in list1:
        if pan==0:
            f.write(child)
        else:
            f.write(child.encode('UTF-8'))
    f.close()

def BIG52GB_path(path,transfer,lan):
    files = os.listdir(path)
    for file_ in files:
        if os.path.isfile(path+file_):
            name=file_
            newname=''
            while not(name.find('.')==-1):
                newname=newname+"."+name[:name.find('.')]
                name=name[name.find('.')+1:]
            #if (file_.find('.ass') >=0 or file_.find('.srt') >=0 or file_.find('.ssa') >=0 or file_.find('.sub') >=0 or file_.find('.smi') >=0 ) and file_[0]!='.' :
            if (name.find('ass') >=0 or name.find('srt') >=0 or name.find('ssa') >=0 or name.find('sub') >=0 or name.find('smi') >=0 ) and file_[0]!='.' :
                print("file=",file_)
                if (len(re.findall(r"S",transfer)) >0 or len(re.findall(r"J",transfer)) >0 or len(re.findall(r"简体",transfer)) >0 or len(re.findall(r"implified",transfer)) >0):
                    if len(re.findall(r"CN",lan)) >0:
                        print("转换为简体\n")
                    else:
                        print("Convert to Simplified\n")
                    BIG52GB(path+file_)
                if (len(re.findall(r"T",transfer)) >0 or len(re.findall(r"F",transfer)) >0 or len(re.findall(r"繁体",transfer)) >0 or len(re.findall(r"raditional",transfer)) >0):
                    if len(re.findall(r"CN",lan)) >0:
                        print("转换为繁体\n")
                    else:
                        print("Convert to Traditional\n")
                    GB2BIG5(path+file_)
if __name__ == '__main__':
    lan  = input("Please choose language: \n(中文请输入CN, EN for English.) \nExample:CN\n")
    if len(re.findall(r"CN",lan)) >0:
        path= input("请输入字幕文件所在文件夹绝对路径.\n例如(Mac): /Users/moyu/Downloads/subtitle\n例如（Windows）: C:\\subtitle\n")
        transfer=input("转换为简体(S)还是繁体(T)？\n例如:S\n")
    elif len(re.findall(r"EN",lan))>0:
        path= input("Please enter the absolute path of the folder where the subtitle file is located\nExample(Mac): /Users/moyu/Downloads/subtitle\nExample（Windows）: C:\\subtitle\n")
        transfer=input("Convert to Simplified(S) or Traditional(T)?\nExample:S\n")
    else:
        print("Error, Thanks for using!")
        exit()
    if (path[len(path)-1]!='/'):
        path=path.strip()+"/"
    print("\n\n_____________START_____________")
    BIG52GB_path(path,transfer,lan)
    en=input("Complete Successfully！")

    '''
    path = sys.argv[1]
    if (path[len(path)-1]!='/'):
        path=path.strip()+"/"
    BIG52GB_path(path)
    '''

