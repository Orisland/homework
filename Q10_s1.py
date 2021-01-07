import os

local = os.getcwd()
xd = "txt\\"
zoo = os.path.join(local,xd)
xd = zoo + "t1.txt"
print(xd)
file = open(xd, encoding="utf-8")
str1 = file.read()
file.close()
file = open(zoo + "t2.txt", encoding="utf-8")
str2 = file.read()
file.close()
str1 = str1 + "\r" +str2

file = open(xd, "a+", encoding="utf-8")
file.write("\r"+str2)
file.close()