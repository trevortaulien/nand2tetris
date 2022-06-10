print("I'm running :)")

import os
import sys

location = sys.argv[1]

stuff = os.listdir(location)

print(stuff)
print('^STUFF^')

def vmFile(file):
    if(file.find('.vm') == -1):
        return False

    return True

importantStuff = filter(vmFile, stuff)

print(importantStuff)

for file in importantStuff:
    with open(location + '/' + file, 'r') as f:
        goods = f.readlines()
        print(goods)

outputPath = sys.argv[1] + '/' + os.path.basename(sys.argv[1]) + '.asm'
lines = ['asasdda','adasdasdasd','adasdadsa']

with open(outputPath, 'w') as w:
    w.writelines(lines)

print(sys.argv[1].replace('.vm', '.asm'))

print("I'm done :)")