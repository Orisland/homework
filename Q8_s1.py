import random

zimu = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]

string = ""
for i in range(6):
    if int(random.randint(0,1)) == 1:
        string += str(random.randint(0,9))
    else:
        string += str(zimu[random.randrange(26)])

print(string)