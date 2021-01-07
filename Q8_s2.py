import random

num1 = float(input("红包总金额："))
num2 = int(input("红包数量"))

list = []

for i in range(num2):
    ran = float(round(random.uniform(0,num1),2))
    if ran > num1:
        ran = num1
        list.append(ran)
    else:
        list.append(ran)
        num1 -= ran

print(list)