# -*- coding:utf-8 -*- 
import urllib2
import urllib
import re

def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print path+' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
        return False

# 定义要创建的目录
mkpath="images\\"
# 调用函数
mkdir(mkpath)

imgurl='https://ottrbutt.com/wallpapers/'
request = urllib2.Request(imgurl)
response = urllib2.urlopen(request)

reg = r'href=\'(.+?\.jpg)\''
imgre = re.compile(reg)
imglist = re.findall(imgre,response.read())

print len(imglist)
for i in range (0,len(imglist)):
    download = imgurl+imglist[i]
    urllib.urlretrieve(download,"./images/%s.jpg" %i )
    print "%s.jpg Got!." %i
