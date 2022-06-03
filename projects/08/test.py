print("I'm running :)")

import os
import sys

location = sys.argv[1]

stuff = os.listdir(location)

print(stuff)

def vmFile(file):
    if(file.find('.vm') == -1):
        return False

    return True

importantStuff = filter(vmFile, stuff)

print(importantStuff)

for file in importantStuff:
    with open(location + file, 'r') as f:
        goods = f.readlines()
        print(goods)

print("I'm done :)")