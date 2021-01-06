#28腿，10头

#鸡为i
i = 0
while True:
    if (2*i + 4*(10-i) == 28):
        break
    else:
        i += 1

result = "鸡:"+str(i)+",兔:"+str(10-i)
print(result)