tokenBag = 'class Main { function void main() { var Array a; var int length; var int i, sum; let length = Keyboard.readInt("HOW MANY NUMBERS? "); let a = Array.new(length); let i = 0; while (i < length) { let a[i] = Keyboard.readInt("ENTER THE NEXT NUMBER: "); let i = i + 1; } let i = 0; let sum = 0; while (i < length) { let sum = sum + a[i]; let i = i + 1; } do Output.printString("THE AVERAGE IS: "); do Output.printInt(sum / length); do Output.println(); return; } }'

def advance():

    global tokenBag

    symbols = {'{' : 'SYMBOL', '}' : 'SYMBOL', '(' : 'SYMBOL', ')' : 'SYMBOL', '[' : 'SYMBOL', 
               ']' : 'SYMBOL', '.' : 'SYMBOL', ',' : 'SYMBOL', ';' : 'SYMBOL', '+' : 'SYMBOL', 
               '-' : 'SYMBOL', '*' : 'SYMBOL', '/' : 'SYMBOL', '&' : 'SYMBOL', '|' : 'SYMBOL', 
               '<' : 'SYMBOL', '>' : 'SYMBOL', '=' : 'SYMBOL', '~' : 'SYMBOL'}

    index = 0
    possibleToken = ''
        
    while(tokenBag[index].isspace()):
        index += 1
    
    # STRING CONSTANT
    if(tokenBag[index] == '"'):
        possibleToken = possibleToken + tokenBag[index]
        index += 1
        while(tokenBag[index] != '"'):
            possibleToken = possibleToken + tokenBag[index]
            index += 1
        possibleToken = possibleToken + tokenBag[index]
        index += 1
        tokenBag = tokenBag[index:]
        return possibleToken

    # IDENTIFIER
    while(tokenBag[index].isalpha() or tokenBag[index] == '_'):
        possibleToken = possibleToken + tokenBag[index]
        if(tokenBag[index + 1] in symbols):
            index += 1
            tokenBag = tokenBag[index:]
            return possibleToken
        index += 1
        while(tokenBag[index].isdigit()):
            possibleToken = possibleToken + tokenBag[index]
            index += 1
        if(tokenBag[index] in symbols):
            index += 1
            tokenBag = tokenBag[index:]
            return possibleToken

    # INT_CONST
    while(tokenBag[index].isdigit()):
        possibleToken = possibleToken + tokenBag[index]
        if(tokenBag[index + 1] in symbols):
            index += 1
            tokenBag = tokenBag[index:]
            return possibleToken
        index += 1

    # SYMBOL
    while(tokenBag[index] in symbols):
        possibleToken = tokenBag[index]
        index += 1
        break

    tokenBag = tokenBag[index:]
    return possibleToken

tokenList = []

while(len(tokenBag) > 0):
#for i in range(100):
    tokenList.append(advance())
    
print(tokenBag)
print(tokenList)