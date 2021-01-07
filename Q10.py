import os
import random
import shutil

local = os.getcwd()
print("get:"+local)
temp = "temp\\"
temp = os.path.join(local,temp)
print("temp:"+temp)
if not os.path.exists(temp):
    print("创建新文件夹")
    os.mkdir(temp)
else:
    print("删除已存在文件夹")
    shutil.rmtree(temp)
    os.mkdir(temp)

for i in range(1,11):
    filename = "n"+str(i)+".txt"
    file = open(temp+filename,"a+")
    str1 = ""
    for i in range(10):
        str1 += str(random.randint(0,20)) + "\r"
    file.write(str1)
    file.close()
    print(filename+"写入完毕")

if not os.path.exists("D:\\python测试文档\\"):
    os.mkdir("D:\\python测试文档\\")
    shutil.copytree(temp,"D:\\python测试文档\\")