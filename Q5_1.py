str = ["软件201_20201103_张三_4507889766.jpg","20201125_软件201_李四_4507887037.jpg","软件201_王五_4507887951_20201133.jpg",
       "软件201_20201108小明——4507887642.jpg","20201147软件201_黄菲菲_4507888888.jpg"]

change= []

for i in range(len(str)):
       change.append(str[i][int(str[i].find("2020")) : int(str[i].find("2020") + 8)])


for i in range(len(change)):
       print(change[i]+".jpg")