from cgi import test
from doctest import OutputChecker


myString = ' class Main { function void main() { var Array a; var int length; var int i, sum; let length = Keyboard.readInt("HOW MANY NUMBERS? "); let a = Array.new(length); let i = 0; while (i < length) { let a[i] = Keyboard.readInt("ENTER THE NEXT NUMBER: "); let i = i + 1; } let i = 0; let sum = 0; while (i < length) { let sum = sum + a[i]; let i = i + 1; } do Output.printString("THE AVERAGE IS: "); do Output.printInt(sum / length); do Output.println(); return; } }'' class Main { function void main() { var Array a; var int length; var int i, sum; let length = Keyboard.readInt("HOW MANY NUMBERS? "); let a = Array.new(length); let i = 0; while (i < length) { let a[i] = Keyboard.readInt("ENTER THE NEXT NUMBER: "); let i = i + 1; } let i = 0; let sum = 0; while (i < length) { let sum = sum + a[i]; let i = i + 1; } do Output.printString("THE AVERAGE IS: "); do Output.printInt(sum / length); do Output.println(); return; } }'

testStr = 'adsd322s'
outputStr = testStr.replace('2s', 'T.xml')
# print(outputStr)

myList = ['abc', ['123', '456']]

for item in myList:
    print(type(item))
