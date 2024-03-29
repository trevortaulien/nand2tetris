print("I'm working :)")

import os
import sys

class Analyzer:

    # sourceJack = []
    # tokenizedJack = []
    # compiledJack = []
    # xmlTokens = []
    # xmlCompiled = []
    # outputPath = 'Replace Me'

    def __init__(self):
        # self._getJack()
        self.sourceJack = []
        self.tokenizedJack = []
        self.compiledJack = []
        self.xmlTokens = []
        self.xmlCompiled = []
        self.outputPath = 'Replace Me'
        pass

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

    def compile(self):
        
        ce = CompilationEngine(self.tokenizedJack)

        ce.startEngine()

        self.compiledJack = ce.compiledJack

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

#        with open(sys.argv[1], 'r') as j:
#            self.sourceJack = j.readlines()

        # flattenFileLists()
        removeInLineComments()
        removeEscapedCharacters()
        removeEmptyLines()
        flattenToString()
        removeBlockComments()
        removeLeadingAndTrailingSpaces()

    def _outputTokensAsXML(self):
        
        outputPath = self.outputPath.replace('.jack','T.xml')

        tokenTypeXML = {'KEYWORD' : 'keyword', 
                     'SYMBOL' : 'symbol', 
                     'IDENTIFIER' : 'identifier', 
                     'INT_CONST' : 'integerConstant',
                     'STRING_CONST' : 'stringConstant'
                     }

        self.xmlTokens.append('<tokens>')

        for token in self.tokenizedJack:
            if(token[1] == '<'):
                token[1] = '&lt;'
            if(token[1] == '>'):
                token[1] = '&gt;'
            if(token[1] == '"'):
                token[1] = '&quot;'
            if(token[1] == '&'):
                token[1] = '&amp;'

            self.xmlTokens.append('<' + tokenTypeXML[token[0]] + '> ' + token[1] + ' </' + tokenTypeXML[token[0]] + '>')

        self.xmlTokens.append('</tokens>')

        with open(outputPath, 'w') as t:
            for token in self.xmlTokens:
                t.write(token + '\n')

    def _outputCompiledAsXML(self):
        outputPath = self.outputPath.replace('.jack', '.xml')

        tokenTypeXML = {'KEYWORD' : 'keyword', 
                     'SYMBOL' : 'symbol', 
                     'IDENTIFIER' : 'identifier', 
                     'INT_CONST' : 'integerConstant',
                     'STRING_CONST' : 'stringConstant'
                     }

        for item in self.compiledJack:
            if isinstance(item, str):
                self.xmlCompiled.append('<' + item + '>')
            else:
                if(item[1] == '<'):
                   item[1] = '&lt;'
                if(item[1] == '>'):
                   item[1] = '&gt;'
                if(item[1] == '"'):
                   item[1] = '&quot;'
                if(item[1] == '&'):
                    item[1] = '&amp;'

                self.xmlCompiled.append('<' + tokenTypeXML[item[0]] + '> ' + item[1] + ' </' + tokenTypeXML[item[0]] + '>')

        with open(outputPath, 'w') as c:
            for item in self.xmlCompiled:
                c.write(item + '\n')

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
            if(self.tokenBag[index] in self.symbols):
                self.tokenBag = self.tokenBag[index:]
                return possibleToken

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

    # index = 0
    # compiledJack = []

    def __init__(self, tokenizedJack):
        self.tokens = tokenizedJack
        self.index = 0
        self.compiledJack = []

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

        self.compiledJack.append('/parameterList')

    def _compileSubroutineBody(self):
        self.compiledJack.append('subroutineBody')
        
        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        if(self.tokens[self.index][1] == 'var'):
            self._compileVarDec()

        if(self.tokens[self.index][1] == 'let' or
           self.tokens[self.index][1] == 'if' or
           self.tokens[self.index][1] == 'while' or
           self.tokens[self.index][1] == 'do' or
           self.tokens[self.index][1] == 'return'):
            self._compileStatements()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append('/subroutineBody')

    def _compileVarDec(self):
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

    def _compileStatements(self):
        self.compiledJack.append('statements')

        while(self.tokens[self.index][1] == 'let' or
              self.tokens[self.index][1] == 'if' or
              self.tokens[self.index][1] == 'while' or
              self.tokens[self.index][1] == 'do' or
              self.tokens[self.index][1] == 'return'):
              
            if(self.tokens[self.index][1] == 'let'):
                self._compileLet()

            elif(self.tokens[self.index][1] == 'if'):
                self._compileIf()

            elif(self.tokens[self.index][1] == 'while'):
                self._compileWhile()

            elif(self.tokens[self.index][1] == 'do'):
                self._compileDo()

            elif(self.tokens[self.index][1] == 'return'):
                self._compileReturn()

        self.compiledJack.append('/statements')

    def _compileLet(self):
        self.compiledJack.append('letStatement')

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        if(self.tokens[self.index][1] == '['):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self._compileExpression()

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self._compileExpression()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append('/letStatement')

    def _compileIf(self):
        self.compiledJack.append('ifStatement')

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self._compileExpression()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self._compileStatements()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        if(self.tokens[self.index][1] == 'else'):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self._compileStatements()

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

        self.compiledJack.append('/ifStatement')

    def _compileWhile(self):
        self.compiledJack.append('whileStatement')

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self._compileExpression()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self._compileStatements()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append('/whileStatement')

    def _compileDo(self):
        self.compiledJack.append('doStatement')

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self._compileSubroutineCall()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append('/doStatement')

    def _compileReturn(self):
        self.compiledJack.append('returnStatement')

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        if(self.tokens[self.index][1] != ';'):
            self._compileExpression()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append('/returnStatement')

    def _compileExpression(self):
        self.compiledJack.append('expression')

        self._compileTerm()

        while(self.tokens[self.index][1] == '+' or
              self.tokens[self.index][1] == '-' or
              self.tokens[self.index][1] == '*' or
              self.tokens[self.index][1] == '/' or
              self.tokens[self.index][1] == '&' or
              self.tokens[self.index][1] == '|' or
              self.tokens[self.index][1] == '<' or
              self.tokens[self.index][1] == '>' or
              self.tokens[self.index][1] == '='):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1
            
            self._compileTerm()

        self.compiledJack.append('/expression')

    def _compileTerm(self):
        self.compiledJack.append('term')
        
        # '(' expression ')' #
        if(self.tokens[self.index][1] == '('):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self._compileExpression()

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append('/term')
            return
        #         #          #

        # (unaryOp term) #
        elif(self.tokens[self.index][1] == '-' or          
           self.tokens[self.index][1] == '~'):
           self.compiledJack.append(self.tokens[self.index])
           self.index += 1

           self._compileTerm()

           self.compiledJack.append('/term')
           return
        #       #        #

        # varName '[' expression ']' #
        elif(self.tokens[self.index + 1][1] == '['):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self._compileExpression()

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append('/term')
            return
        #            #               #

        elif(self.tokens[self.index + 1][1] == '(' or
             self.tokens[self.index + 1][1] == '.'):
             
             self._compileSubroutineCall()

             self.compiledJack.append('/term')

        else:
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append('/term')

    def _compileSubroutineCall(self):
        # subroutineName '(' expressionList ')' #
        if(self.tokens[self.index + 1][1] == '('):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self._compileExpressionList()

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            return

        # (className | varName) '.' subroutineName '(' expressionList ')' #
        elif(self.tokens[self.index + 1][1] == '.'):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self._compileExpressionList()

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            return

    def _compileExpressionList(self):
        self.compiledJack.append('expressionList')

        if(self.tokens[self.index][1] == ')'):
            self.compiledJack.append('/expressionList')
            return

        self._compileExpression()

        while(self.tokens[self.index][1] == ','):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self._compileExpression()

        self.compiledJack.append('/expressionList')

def singleInArg():

    vmMaker = Analyzer()

    with open(sys.argv[1], 'r') as j:
        vmMaker.sourceJack = j.readlines()

    vmMaker.outputPath = sys.argv[1]
    vmMaker._getJack()
    vmMaker.tokenize()
    vmMaker.compile()
    vmMaker._outputTokensAsXML()
    vmMaker._outputCompiledAsXML()

def checkJackFile(fileName):
    if(fileName.find('.jack') == -1):
        return False
    return True

def multiInArg():

    dirContents = os.listdir(sys.argv[1])
    jackFileNames = list(filter(checkJackFile, dirContents))

    for file in jackFileNames:
        vmMaker = Analyzer()

        with open(sys.argv[1] + '/' + file, 'r') as j:
            vmMaker.sourceJack = j.readlines()

        vmMaker.outputPath = sys.argv[1] + '/'  + file
        vmMaker._getJack()
        vmMaker.tokenize()
        vmMaker.compile()
        vmMaker._outputTokensAsXML()
        vmMaker._outputCompiledAsXML()

def run():
    inArg = sys.argv[1]
    if(os.path.isfile(inArg) == True):
        singleInArg()
    else:
        multiInArg()

run()

# vmMaker = Analyzer()
# vmMaker.tokenize()
# vmMaker.compile()
# vmMaker._outputTokensAsXML()
# vmMaker._outputCompiledAsXML()

print("I'm done :)")