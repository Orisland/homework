import random
#在随机的15和不重复的数字里，猜5数字

num = []
for x in range(15):
    while True:
        num1 = random.randint(1, 100)
        if num1 not in num:
            num.append(num1)
            break
        else:
            continue

print(num)

guess = []
for i in range(5):
    guessnum = input("input number:")
    guess.append(int(guessnum))


res = []
for i in guess:
    if i not in num:
        continue
    if i in num:
        res.append(i)

print("猜中的数字为:" + str(res))