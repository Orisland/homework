import os
import random
import shutil

if not os.path.exists("\\temp"):
    os.mkdir("\\temp")
    print(os.path.exists("\\temp"))
else:
    print("删除已存在文件夹")
    shutil.rmtree("\\temp")
    os.mkdir("\\temp")
    print(os.path.exists("\\temp"))

for i in range(10):
    filename = "n"+str(i)+".txt"
    file = open(r"/temp/"+filename,"a+")
    str1 = ""
    for i in range(10):
        str1 += str(random.randint(0,20)) + "\r"
    file.write(str1)
    file.close()
    print(filename+"写入完毕")