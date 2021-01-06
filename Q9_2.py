import random

list = []

for i in range(5):
    list.append(random.randint(0,20))

print(list)

guess = []
for i in range(5):
    while True:
        try:
            num = int(input("输入整数"))
            guess.append(num)
            break
        except ValueError:
            print("重新输入")
            continue

sucess = []
for i in range(len(guess)):
    if guess[i] in list:
        sucess.append(guess[i])
    else:
        continue

print("猜对的数字:" + str(sucess))