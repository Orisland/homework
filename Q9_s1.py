list = ["1000", "2000", "空调", "3000"]

add = 0
for i in range(len(list)):
    try:
        add += int(list[i])
    except ValueError:
        pass

print(add)