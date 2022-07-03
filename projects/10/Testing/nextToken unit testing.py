

class Token():

    def __init__(self):   
        self.tokenBag = ' class Main { function void main() { var Array a; var int length; var int i, sum; let length = Keyboard.readInt("HOW MANY NUMBERS? "); let a = Array.new(length); let i = 0; while (i < length) { let a[i] = Keyboard.readInt("ENTER THE NEXT NUMBER: "); let i = i + 1; } let i = 0; let sum = 0; while (i < length) { let sum = sum + a[i]; let i = i + 1; } do Output.printString("THE AVERAGE IS: "); do Output.printInt(sum / length); do Output.println(); return; } }'

    def nextToken(self):
            token = ['Replace', 'Me'] # format of some token is [type, token]
            possibleToken = ''
            tokenStatus = '-1'
            index = 0

            while(tokenStatus == '-1'):
                possibleToken = possibleToken + self.tokenBag[index]
                tokenStatus = self.ValidToken(possibleToken)
                index += 1
                if(index > 10):
                    print("I'm quiting")
                    quit()

            self.tokenBag = self.tokenBag.remove(possibleToken)
            token[0] = tokenStatus
            token[1] = possibleToken
            token[1] = token[1].strip()

            return token

    def ValidToken(self, possibleToken):
        print("Checking Valid Token")
        print("Possible Token is:" + possibleToken)
        if(possibleToken[0] == ' '):
            possibleToken = possibleToken[1:]
            if(len(possibleToken) < 1):
                return '-1'
        elif(self.keyword(possibleToken) != '-1'):
            return self.keyword(possibleToken)
        elif(self.symbol(possibleToken) != '-1'):
            return self.symbol(possibleToken)
        elif(self.identifier(possibleToken) != '-1'):
            return self.identifier(possibleToken)
        elif(self.intVal(possibleToken) != '-1'):
            return self.intVal(possibleToken)
        else:
            return self.stringVal(possibleToken)

    def keyword(self, possibleToken):
        keywords = {'class'  : 'KEYWORD', 'constructor': 'KEYWORD', 'function': 'KEYWORD', 'method': 'KEYWORD', 'field'  : 'KEYWORD',
                    'static' : 'KEYWORD', 'var'        : 'KEYWORD', 'int'     : 'KEYWORD', 'char'  : 'KEYWORD', 'boolean': 'KEYWORD',
                    'void'   : 'KEYWORD', 'true'       : 'KEYWORD', 'false'   : 'KEYWORD', 'null'  : 'KEYWORD', 'this'   : 'KEYWORD',
                    'let'    : 'KEYWORD', 'do'         : 'KEYWORD', 'if'      : 'KEYWORD', 'else'  : 'KEYWORD', 'while'  : 'KEYWORD',
                    'return' : 'KEYWORD'}

        possibleToken = possibleToken.strip()
        
        if possibleToken in keywords:
            return 'KEYWORD'
        else:
            return '-1'

    def symbol(self, possibleToken):
        symbols = {'{' : 'SYMBOL', '}' : 'SYMBOL', '(' : 'SYMBOL', ')' : 'SYMBOL', '[' : 'SYMBOL', 
                   ']' : 'SYMBOL', '.' : 'SYMBOL', ',' : 'SYMBOL', ';' : 'SYMBOL', '+' : 'SYMBOL', 
                   '-' : 'SYMBOL', '*' : 'SYMBOL', '/' : 'SYMBOL', '&' : 'SYMBOL', '|' : 'SYMBOL', 
                   '<' : 'SYMBOL', '>' : 'SYMBOL', '=' : 'SYMBOL', '~' : 'SYMBOL'}

        possibleToken = possibleToken.strip()

        if possibleToken in symbols:
            return 'SYMBOL'
        else:
            return '-1'

    def identifier(self, possibleToken):
        if(possibleToken[-1] == ' '):
            return 'IDENTIFIER'
        elif(self.symbol(possibleToken[-1]) == 'SYMBOL'):
            return 'IDENTIFIER'
        else:
            return '-1'

    def intVal(self, possibleToken):
        return '-1'

    def stringVal(self, possibleToken):
        return '-1'

tokens = []
tok = Token()
for i in range(18):
    token = tok.nextToken()
    tokens.append(token)
    print(token)
    print(tok.tokenBag)
    print('\n')
    i += 1

print(tokens)