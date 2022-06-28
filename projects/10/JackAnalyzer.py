print("I'm working :)")

import os
import sys

class Analyzer:

    sourceJack = []

    def __init__(self):
        self.getJack()

    def tokenize(self):
        
        tokenSleeve = []

        tokenizer = Tokenizer(self.sourceJack)

        i = 0
        while(len(tokenizer.tokenBag) != 0):
            token = tokenizer.nextToken()
            tokenSleeve.append(token)
            i +=1
            if(i > 100):
                quit()

    def compile(self):
        pass

    def outputVM(self):
        pass

    def getJack(self):

        def flattenFileLists():
            temp = []
            for fileList in self.sourceJack:
                for item in fileList:
                    temp.append(item)

            self.sourceJack = temp

        def removeInLineComments():
            temp = []
            for item in self.sourceJack:
                if(item.find('//') != -1):
                    splitItem = item.split('//')
                    temp.append(splitItem[0])
                else:
                    temp.append(item)

            self.sourceJack = temp

        def removeEscapedCharacters():
            self.sourceJack = [item.strip() for item in self.sourceJack]

        def removeEmptyLines():
            self.sourceJack = [item for item in self.sourceJack if item != '']

        def flattenToString():
            temp = ''
            for item in self.sourceJack:
                temp = temp + item + ' '

            self.sourceJack = temp

        def removeBlockComments():
            while(self.sourceJack.find('/*') != -1):
                blockCommentStart = self.sourceJack.find('/*')
                blockCommentEnd = self.sourceJack.find('*/')
                temp = self.sourceJack[:blockCommentStart] + self.sourceJack[blockCommentEnd + 2:]
                self.sourceJack = temp

        def removeLeadingAndTrailingSpaces():
            self.sourceJack = self.sourceJack.strip()

        dirContents = os.listdir(sys.argv[1])
        
        with open(sys.argv[1] + "Main.jack", 'r') as m:
            sourceMain = m.readlines()

        self.sourceJack.append(sourceMain)
        dirContents.remove("Main.jack")

        for file in dirContents:
            if(file.find(".jack") != -1):
                with open(sys.argv[1] + file, 'r') as a:
                    sourceFile = a.readlines()
                    self.sourceJack.append(sourceFile)

        flattenFileLists()
        removeInLineComments()
        removeEscapedCharacters()
        removeEmptyLines()
        flattenToString()
        removeBlockComments()
        removeLeadingAndTrailingSpaces()

class Tokenizer(Analyzer):

    currentToken = ''

    def __init__(self, sourceJack):
        self.tokenBag = sourceJack
        

    def nextToken(self):
        token = ['Replace', 'Me'] # format of some token is [type, token]
        possibleToken = ''
        tokenStatus = '-1'
        index = 0

        while(tokenStatus == '-1'):
            possibleToken = possibleToken + self.tokenBag[index]
            tokenStatus = self.ValidToken(possibleToken)
            index += 1
            if(index > 100):
                quit()

        self.tokenBag[index:]
        token[0] = tokenStatus
        token[1] = possibleToken
        token[1].strip()
        print(token)

        return token

    def ValidToken(self, possibleToken):
        valid = '-1'
        valid = self.keyword(possibleToken)
        valid = self.symbol(possibleToken)
        valid = self.identifier(possibleToken)
        valid = self.intVal(possibleToken)
        valid = self.stringVal(possibleToken)

        return valid

    def keyword(self, possibleToken):
        keywords = {'class'  : 'KEYWORD', 'constructor': 'KEYWORD', 'function': 'KEYWORD', 'method': 'KEYWORD', 'field'  : 'KEYWORD',
                    'static' : 'KEYWORD', 'var'        : 'KEYWORD', 'int'     : 'KEYWORD', 'char'  : 'KEYWORD', 'boolean': 'KEYWORD',
                    'void'   : 'KEYWORD', 'true'       : 'KEYWORD', 'false'   : 'KEYWORD', 'null'  : 'KEYWORD', 'this'   : 'KEYWORD',
                    'let'    : 'KEYWORD', 'do'         : 'KEYWORD', 'if'      : 'KEYWORD', 'else'  : 'KEYWORD', 'while'  : 'KEYWORD',
                    'return' : 'KEYWORD'}

        possibleToken.strip()

        if(possibleToken == ' '):
            return '-1'
        elif(keywords[possibleToken]):
            return 'KEYWORD'
        else:
            return '-1'

    def symbol(self, possibleToken):
        symbols = {'{' : 'SYMBOL', '}' : 'SYMBOL', '(' : 'SYMBOL', ')' : 'SYMBOL', '[' : 'SYMBOL', 
                    ']' : 'SYMBOL', '.' : 'SYMBOL', ',' : 'SYMBOL', ';' : 'SYMBOL', '+' : 'SYMBOL', 
                    '-' : 'SYMBOL', '*' : 'SYMBOL', '/' : 'SYMBOL', '&' : 'SYMBOL', '|' : 'SYMBOL', 
                    '<' : 'SYMBOL', '>' : 'SYMBOL', '=' : 'SYMBOL', '~' : 'SYMBOL'}

        possibleToken.strip()

        if(possibleToken == ' '):
            return '-1'
        elif(symbols[possibleToken]):
            return 'SYMBOL'
        else:
            return '-1'

    def identifier(self, possibleToken):
        pass

    def intVal(self, possibleToken):
        pass

    def stringVal(self, possibleToken):
        pass

class CompilationEngine(Analyzer):

    def __init__(self):
        pass

    def compileClass(self):
        pass

    def compileClassVarDec(self):
        pass

    def compileSubroutine(self):
        pass

    def compileParameterList(self):
        pass

    def compileSubroutineBody(self):
        pass

    def compileLet(self):
        pass

    def compileIf(self):
        pass

    def compileWhile(self):
        pass

    def compileDo(self):
        pass

    def compileReturn(self):
        pass

    def compileExpression(self):
        pass

    def compileTerm(self):
        pass

    def compuleExpressionList(self):
        pass

vmMaker = Analyzer()
#vmMaker.tokenize()
#vmMaker.compile()
#vmMaker.outputVM()

print(vmMaker.sourceJack)


print("I'm done :)")