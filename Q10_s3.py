import os
import shutil

path = os.getcwd()
path1 = os.path.join(path,"temp\\ch10\\")

if not os.path.exists(path1):
    os.mkdir(path1)
else:
    print("已存在")
    shutil.rmtree(path1)
    os.mkdir(path1)

for i in range(1,11):
    k = str(i)
    k = k.zfill(3)
    k = "文件夹"+k
    os.mkdir(os.path.join(path1, k))