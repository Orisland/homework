numlist = []
def numcatch(nums):
    numes = 0
    for i in range(len(nums)):
        numes += nums[i]
    return numes

def inputnum(num):
    for i in range(num):
        while True:
            try:
                num1 = int(input("输入数字:"))
                break
            except ValueError:
                continue
        numlist.append(num1)

while True:
    try:
        num = int(input("要输入几个数字?"))
        break
    except ValueError:
        continue


inputnum(num)
print(numcatch(numlist))