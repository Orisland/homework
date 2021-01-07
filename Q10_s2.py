import datetime
import shutil
import os

time = datetime.datetime.now().strftime("%Y-%m-%d")

path1 = os.getcwd()
path2 = os.path.join(path1, "temp\\")
if not os.path.exists(path2):
    os.mkdir(path2)
else:
    print("已存在")

path3 = os.path.join(path2, datetime.datetime.now().strftime("%Y"))
if not os.path.exists(path3):
    os.mkdir(path3)
else:
    print("已存在")

path4 = os.path.join(path3, datetime.datetime.now().strftime("%Y-%m"))
if not os.path.exists(path4):
    os.mkdir(path4)
else:
    print("已存在")

path5 = os.path.join(path4, datetime.datetime.now().strftime("%Y-%m-%d"))
if not os.path.exists(path5):
    os.mkdir(path5)
else:
    print("已存在")
