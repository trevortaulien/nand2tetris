segmentName = {'FIELD' : 'this'  , 'ARG' : 'argument',
                   'STATIC': 'static', 'VAR' : 'local'   }

print(segmentName['FIELD'])

myList = [1,'bob',3,5,7,'tom']

for item in myList:
    if(item == 'bob'):
        myList[myList.index('bob')] = 'notbob'

print(myList)

myString = 'Score: 0'

for char in myString:
    print(ord(char))