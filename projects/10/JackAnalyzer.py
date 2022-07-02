print("I'm working :)")

import os
import sys
from lxml import etree

class Analyzer:

    sourceJack = []
    tokenizedJack = []
    compiledJack = []
    xmlTokens = []
    xmlCompiled = []

    def __init__(self):
        self._getJack()

    def tokenize(self):

        tokenSleeve = []

        tokenizer = Tokenizer(self.sourceJack)

        while(len(tokenizer.tokenBag) > 0):
            tokenSleeve.append(tokenizer.advance())

        for token in tokenSleeve:
            tokenType = tokenizer.tokenType(token)
            if(tokenType == 'STRING_CONST'):
                self.tokenizedJack.append([tokenType, tokenizer._stringVal(token)])
            else:
                self.tokenizedJack.append([tokenType, token])

        self._outputTokensAsXML()

    def compile(self):
        
        ce = CompilationEngine(self.tokenizedJack)

        ce.startEngine()

        self.compiledJack = ce.compiledJack

        self._outputCompiledAsXML()

    def outputVM(self):
        pass

    def _getJack(self):

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

        ### THIS BLOCK OPENS ALL FILES IN DIRECTORY AND APPENDS ALL OF THE JACK TO ONE BIG LIST ###
        # dirContents = os.listdir(sys.argv[1])
        
        # with open(sys.argv[1] + "Main.jack", 'r') as m:
        #     sourceMain = m.readlines()

        # self.sourceJack.append(sourceMain)
        # dirContents.remove("Main.jack")

        # for file in dirContents:
        #     if(file.find(".jack") != -1):
        #         with open(sys.argv[1] + file, 'r') as a:
        #             sourceFile = a.readlines()
        #             self.sourceJack.append(sourceFile)
        ###########################################################################################

        with open(sys.argv[1], 'r') as j:
            self.sourceJack = j.readlines()

        # flattenFileLists()
        removeInLineComments()
        removeEscapedCharacters()
        removeEmptyLines()
        flattenToString()
        removeBlockComments()
        removeLeadingAndTrailingSpaces()

    def _outputTokensAsXML(self):
        
        outputPath = sys.argv[1].replace('.jack','T_.xml')

        tokenTypeXML = {'KEYWORD' : 'keyword', 
                     'SYMBOL' : 'symbol', 
                     'IDENTIFIER' : 'identifier', 
                     'INT_CONST' : 'integerConstant',
                     'STRING_CONST' : 'stringConstant'
                     }

        self.xmlTokens.append('<tokens>')

        for token in self.tokenizedJack:
            self.xmlTokens.append('<' + tokenTypeXML[token[0]] + '> ' + token[1] + ' </' + tokenTypeXML[token[0]] + '>')

        self.xmlTokens.append('</tokens>')

        with open(outputPath, 'w') as t:
            for token in self.xmlTokens:
                t.write(token + '\n')

    def _outputCompiledAsXML(self):
        outputPath = sys.argv[1].replace('.jack', '_.xml')

        for item in self.compiledJack:
            if isinstance(item, str):
                self.xmlCompiled.append('<' + item + '>')
            else:
                self.xmlCompiled.append('<' + item[0].lower() + '> ' + item[1] + ' </' + item[0].lower() + '>')

        with open(outputPath, 'w') as c:
            for item in self.xmlCompiled:
                c.write(item + '\n')

        tree = etree.parse(outputPath)
        self.xmlCompiled = etree.tostring(tree, pretty_print = True, encoding = str)        

        with open(outputPath, 'w') as s:
            s.write(self.xmlCompiled)

class Tokenizer(Analyzer):

    symbols = {'{' : 0 , '}' : 1 , '(' : 2 , ')' : 3 , '[' : 4 , 
               ']' : 5 , '.' : 6 , ',' : 7 , ';' : 8 , '+' : 9 , 
               '-' : 10, '*' : 11, '/' : 12, '&' : 13, '|' : 14, 
               '<' : 15, '>' : 16, '=' : 17, '~' : 18
              }

    keywords = {'class'  : 0 , 'constructor': 1 , 'function': 2 , 'method': 3 , 'field'  : 4 ,
                'static' : 5 , 'var'        : 6 , 'int'     : 7 , 'char'  : 8 , 'boolean': 9 ,
                'void'   : 10, 'true'       : 11, 'false'   : 12, 'null'  : 13, 'this'   : 14,
                'let'    : 15, 'do'         : 16, 'if'      : 17, 'else'  : 18, 'while'  : 19,
                'return' : 20
               }

    def __init__(self, sourceJack):
        self.tokenBag = sourceJack
        
    def advance(self):

        index = 0
        possibleToken = ''
            
        while(self.tokenBag[index].isspace()):
            index += 1
        
        # STRING CONSTANT
        if(self.tokenBag[index] == '"'):
            possibleToken = possibleToken + self.tokenBag[index]
            index += 1
            while(self.tokenBag[index] != '"'):
                possibleToken = possibleToken + self.tokenBag[index]
                index += 1
            possibleToken = possibleToken + self.tokenBag[index]
            index += 1
            self.tokenBag = self.tokenBag[index:]
            return possibleToken

        # IDENTIFIER  
        while(self.tokenBag[index].isalpha() or self.tokenBag[index] == '_'):
            possibleToken = possibleToken + self.tokenBag[index]
            if(self.tokenBag[index + 1] in self.symbols):
                index += 1
                self.tokenBag = self.tokenBag[index:]
                return possibleToken
            index += 1
            while(self.tokenBag[index].isdigit()):
                possibleToken = possibleToken + self.tokenBag[index]
                index += 1

        # INT_CONST
        while(self.tokenBag[index].isdigit()):
            possibleToken = possibleToken + self.tokenBag[index]
            if(self.tokenBag[index + 1] in self.symbols):
                index += 1
                self.tokenBag = self.tokenBag[index:]
                return possibleToken
            index += 1

        # SYMBOL
        while(self.tokenBag[index] in self.symbols):
            possibleToken = self.tokenBag[index]
            index += 1
            break

        self.tokenBag = self.tokenBag[index:]
        return possibleToken

    def tokenType(self, token):
        if(token in self.keywords):
            return 'KEYWORD'
        elif(token in self.symbols):
            return 'SYMBOL'
        elif(token[0] == '"' and token[-1] == '"'):
            return 'STRING_CONST'
        elif(token.isdigit()):
            return 'INT_CONST'
        else:
            return 'IDENTIFIER'

    def _keyWord(self):
        pass

    def _symbol(self):
        pass

    def _identifier(self):
        pass

    def _intVal(self, token):
        return int(token)

    def _stringVal(self, token):
        return token[1:-1]

class CompilationEngine(Analyzer):

    index = 0
    compiledJack = []

    def __init__(self, tokenizedJack):
        self.tokens = tokenizedJack

    def startEngine(self):
        self._compileClass()

    def _compileClass(self):
        self.compiledJack.append('class')

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        while(self.tokens[self.index][1] == 'static' or
              self.tokens[self.index][1] == 'field'):
            
            self._compileClassVarDec()

        while(self.tokens[self.index][1] == 'constructor' or
              self.tokens[self.index][1] == 'function'    or
              self.tokens[self.index][1] == 'method'):
            
            self._compileSubroutineDec()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1     # this increment may be unnecessary

        self.compiledJack.append('/class')

    def _compileClassVarDec(self):
        self.compiledJack.append('classVarDec')

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1
        
        while(self.tokens[self.index][1] == ','):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append('/classVarDec')

    def _compileSubroutineDec(self):
        self.compiledJack.append('subroutineDec')

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self._compileParameterList()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self._compileSubroutineBody()

        self.compiledJack.append('/subroutineDec')

    def _compileParameterList(self):
        self.compiledJack.append('parameterList')

        if(self.tokens[self.index][1] == ')'):
            self.compiledJack.append('/parameterList')
            return
        
        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        while(self.tokens[self.index][1] == ','):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1
            print(self.tokens[self.index])

        self.compiledJack.append('/parameterList')

    def _compileSubroutineBody(self):
        self.compiledJack.append('subroutineBody')
        
        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        # varDec #
        while(self.tokens[self.index][1] == 'var'):
            self.compiledJack.append('varDec')

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            while(self.tokens[self.index][1] == ','):
                self.compiledJack.append(self.tokens[self.index])
                self.index += 1

                self.compiledJack.append(self.tokens[self.index])
                self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append('/varDec')
        #   #   #

        # statements #

        self.compiledJack.append('/subroutineBody')

    def _compileLet(self):
        pass

    def _compileIf(self):
        pass

    def _compileWhile(self):
        pass

    def _compileDo(self):
        pass

    def _compileReturn(self):
        pass

    def _compileExpression(self):
        pass

    def _compileTerm(self):
        pass

    def _compuleExpressionList(self):
        pass

vmMaker = Analyzer()
vmMaker.tokenize()
vmMaker.compile()
#vmMaker.outputVM()


# print(vmMaker.tokenizedJack)
print('\n')
print(vmMaker.compiledJack)

print("I'm done :)")