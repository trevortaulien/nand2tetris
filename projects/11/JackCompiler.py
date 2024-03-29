print("I'm working :)")

import sys
import os

class Analyzer():

    # sourceJack = []
    # tokenizedJack = []
    # compiledJack = []
    # compiledVM = []
    # xmlTokens = []
    # xmlCompiled = []
    # outputPath = 'Replace Me'

    def __init__(self):
        # self._getJack()
        self.sourceJack = []
        self.tokenizedJack = []
        self.compiledJack = []
        self.compiledVM = []
        self.xmlTokens = []
        self.xmlCompiled = []
        self.outputPath = 'Replace Me'
        pass

    def tokenize(self):

        tokenSleeve = []

        tokenizer = Tokenizer(self.sourceJack)

        while(len(tokenizer.tokenBag) > 0):
            tokenSleeve.append(tokenizer.advance())

        # self.tokenizedJack = []

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
        self.compiledVM = ce.getCompiledVM()

    def outputVM(self):
        outputPath = self.outputPath.replace('.jack', '.vm')

        with open(outputPath, 'w') as v:
            for vmCommand in self.compiledVM:
                v.write(vmCommand + '\n')

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
        
        outputPath = self.outputPath.replace('.jack','T_.xml')

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
        outputPath = self.outputPath.replace('.jack', '_.xml')

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

class Tokenizer():

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

class SymbolTable():

    def __init__(self):
        self.fieldOrArg = []
        self.staticOrVar = []    

    def reset(self):
        self.fieldOrArg = []
        self.staticOrVar = []

    def define(self, name, type, kind):
        if(kind == 'FIELD' or kind == 'ARG'):
            self.fieldOrArg.append([name,type,kind])
        elif(kind == 'STATIC' or kind == 'VAR'):
            self.staticOrVar.append([name,type,kind])

    def varCount(self, kind):
        count = 0
        if(kind == 'FIELD'):
            for entry in self.fieldOrArg:
                if(entry[2] == 'FIELD'):
                    count += 1
            return count
        elif(kind == 'ARG'):
            for entry in self.fieldOrArg:
                if(entry[2] == 'ARG'):
                    count += 1
            return count
        elif(kind == 'STATIC'):
            for entry in self.staticOrVar:
                if(entry[2] == 'STATIC'):
                    count += 1
            return count
        elif(kind == 'VAR'):
            for entry in self.staticOrVar:
                if(entry[2] == 'VAR'):
                    count += 1
            return count

    def kindOf(self, name):
        for entry in self.fieldOrArg:
            if(entry[0] == name):
                return entry[2]
        for entry in self.staticOrVar:
            if(entry[0] == name):
                return entry[2]

    def typeOf(self, name):
        for entry in self.fieldOrArg:
            if(entry[0] == name):
                return entry[1]
        for entry in self.staticOrVar:
            if(entry[0] == name):
                return entry[1]

    def indexOf(self, name):
        for index, entry in enumerate(self.fieldOrArg):
            if(entry[0] == name):
                return index
        for index, entry in enumerate(self.staticOrVar):
            if(entry[0] == name):
                return index
        return -1

class VMWriter():

    # compiledVM = []

    segments = {'CONSTANT' : 'constant', 'ARGUMENT' : 'argument', 'LOCAL'   : 'local'  , 'STATIC' : 'static',
                'THIS'     : 'this'    , 'THAT'     : 'that'    , 'POINTER' : 'pointer', 'TEMP'   : 'temp'  ,
                'FIELD'    : 'this'    , 'ARG'      : 'argument', 'VAR'     : 'local'  }
    commands = {'ADD' : 'add', 'SUB' : 'sub', 'NEG' : 'neg',
                'EQ'  : 'eq' , 'GT'  : 'gt' , 'LT'  : 'lt' ,
                'AND' : 'and', 'OR'  : 'or' , 'NOT' : 'not',
                '+'   : 'add', '-'   : 'neg', '&'   : 'and',
                '|'   : 'or' , '<'   : 'lt' , '>'   : 'gt' ,
                '='   : 'eq' , '~'   : 'not'}


    def __init__(self):
        self.compiledVM = []
        pass

    def writePush(self, segment, index):
        self.compiledVM.append('push ' + self.segments[segment] + ' ' + str(index))

    def writePop(self, segment, index):
        self.compiledVM.append('pop ' + self.segments[segment] + ' ' + str(index))

    def writeArithmetic(self, command):
        if(command == '*'):
            self.writeCall('Math.multiply', 2)
        elif(command == '/'):
            self.writeCall('Math.divide', 2)
        else:
            self.compiledVM.append(self.commands[command])

    def writeLabel(self, label):
        self.compiledVM.append('label ' + label)

    def writeGoto(self, label):
        self.compiledVM.append('goto ' + label)

    def writeIf(self, label):
        self.compiledVM.append('if-goto ' + label)

    def writeCall(self, name, nVars):
        self.compiledVM.append('call ' + name + ' ' + str(nVars))

    def writeFunction(self, name, nVars):
        self.compiledVM.append('function ' + name + ' ' + str(nVars))

    def writeReturn(self):
        self.compiledVM.append('return')

    def writePlaceHolder(self, placeholder):
        self.compiledVM.append(placeholder)

    def replacePlaceHolder(self, placeholder, replacement):
        for command in self.compiledVM:
            if(command == placeholder):
                self.compiledVM[self.compiledVM.index(command)] = replacement

class CompilationEngine():

    index = 0
    compiledJack = []
    className = 'replace me'
    labelIndex = 0
    label = 'replace me'

    def __init__(self, tokenizedJack):
        self.tokens = tokenizedJack
        self.classST = SymbolTable()
        self.subroutineST = SymbolTable()
        self.vmWriter = VMWriter()

    def startEngine(self):
        self._compileClass()

    def _compileClass(self):
        self.compiledJack.append('class')

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.className = self.tokens[self.index][1]

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        while(self.tokens[self.index][1] == 'static' or
              self.tokens[self.index][1] == 'field'):
            
            self._compileClassVarDec()

        # print('self.classST.fieldOrArg: ')
        # print(self.classST.fieldOrArg)
        # print('\n' + 'self.classST.staticOrVar: ')
        # print(self.classST.staticOrVar)   

        while(self.tokens[self.index][1] == 'constructor' or
              self.tokens[self.index][1] == 'function'    or
              self.tokens[self.index][1] == 'method'):
            
            self._compileSubroutineDec()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append('/class')

    def _compileClassVarDec(self):
        self.compiledJack.append('classVarDec')

        if(self.tokens[self.index][1] == 'static'):
            symbolKind = 'STATIC'
        if(self.tokens[self.index][1] == 'field'):
            symbolKind = 'FIELD'

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        symbolType = self.tokens[self.index][1]

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        symbolName = self.tokens[self.index][1]

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.classST.define(symbolName, symbolType, symbolKind)
        
        while(self.tokens[self.index][1] == ','):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            symbolName = self.tokens[self.index][1]

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.classST.define(symbolName, symbolType, symbolKind)

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append('/classVarDec')

    def _compileSubroutineDec(self):
        self.compiledJack.append('subroutineDec')

        self.subroutineCategory = self.tokens[self.index][1]

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.subroutineType = self.tokens[self.index][1]

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        subroutineName = self.tokens[self.index][1]

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        nVars = self._compileParameterList()

        # print('\n' + 'self.subroutineST.fieldOrArg: ')
        # print(self.subroutineST.fieldOrArg)

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.vmWriter.writePlaceHolder(self.className + '.' + subroutineName)

        if(self.subroutineCategory == 'constructor'):
            self.vmWriter.writePush('CONSTANT', self.classST.varCount('FIELD'))
            self.vmWriter.writeCall('Memory.alloc', 1)
            self.vmWriter.writePop('POINTER', 0)

        if(self.subroutineCategory == 'method'):
            self.vmWriter.writePush('ARGUMENT', 0)
            self.vmWriter.writePop('POINTER', 0)

        self._compileSubroutineBody()

        # print('\n' + 'self.subroutineST.staticOrVar: ')
        # print(self.subroutineST.staticOrVar)

        self.vmWriter.replacePlaceHolder(self.className + '.' + subroutineName, 'function ' + self.className + '.' + subroutineName + ' ' + str(self.subroutineST.varCount('VAR')))

        self.subroutineST.reset()

        self.compiledJack.append('/subroutineDec')

    def _compileParameterList(self):
        self.compiledJack.append('parameterList')

        nVars = 0

        if(self.tokens[self.index - 4][1] == 'method'):
            self.subroutineST.define('this', self.className, 'ARG')

        if(self.tokens[self.index][1] == ')'):
            self.compiledJack.append('/parameterList')
            return nVars 
        
        subroutineArgType = self.tokens[self.index][1]

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        subroutineArgName = self.tokens[self.index][1]

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        nVars += 1

        self.subroutineST.define(subroutineArgName, subroutineArgType, 'ARG')

        while(self.tokens[self.index][1] == ','):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            subroutineArgType = self.tokens[self.index][1]

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            subroutineArgName = self.tokens[self.index][1]

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            nVars += 1

            self.subroutineST.define(subroutineArgName, subroutineArgType, 'ARG')

        self.compiledJack.append('/parameterList')

        return nVars

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

            subroutineVarType = self.tokens[self.index][1]

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            subroutineVarName = self.tokens[self.index][1]

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.subroutineST.define(subroutineVarName, subroutineVarType, 'VAR')

            while(self.tokens[self.index][1] == ','):
                self.compiledJack.append(self.tokens[self.index])
                self.index += 1

                subroutineVarName = self.tokens[self.index][1]

                self.compiledJack.append(self.tokens[self.index])
                self.index += 1

                self.subroutineST.define(subroutineVarName, subroutineVarType, 'VAR')

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

        varName = self.tokens[self.index][1]

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        arrayStatus = -1

        if(self.tokens[self.index][1] == '['):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            arrayStatus = 1

            if(self.subroutineST.indexOf(varName) != -1):
                self.vmWriter.writePush(self.subroutineST.kindOf(varName), self.subroutineST.indexOf(varName))
            else:
                self.vmWriter.writePush(self.classST.kindOf(varName), self.classST.indexOf(varName))

            self._compileExpression()

            self.vmWriter.writeArithmetic('ADD')

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self._compileExpression()

        if(arrayStatus == 1):
            self.vmWriter.writePop('TEMP', 0)
            self.vmWriter.writePop('POINTER', 1)
            self.vmWriter.writePush('TEMP', 0)
            self.vmWriter.writePop('THAT', 0)

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append('/letStatement')
            return

        if(self.subroutineST.indexOf(varName) != -1):
            self.vmWriter.writePop(self.subroutineST.kindOf(varName), self.subroutineST.indexOf(varName))
        else:
            self.vmWriter.writePop(self.classST.kindOf(varName), self.classST.indexOf(varName))

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

        L1 = self._nextLabel()
        L2 = self._nextLabel()

        self.vmWriter.writeArithmetic('NOT')
        self.vmWriter.writeIf(L1)

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self._compileStatements()

        self.vmWriter.writeGoto(L2)
        self.vmWriter.writeLabel(L1)

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        if(self.tokens[self.index][1] == 'else'):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self._compileStatements()

            self.vmWriter.writeLabel(L2)

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1
        else:
            self.vmWriter.writeLabel(L2)

        self.compiledJack.append('/ifStatement')

    def _compileWhile(self):
        self.compiledJack.append('whileStatement')

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        L1 = self._nextLabel()
        L2 = self._nextLabel()

        self.vmWriter.writeLabel(L1)

        self._compileExpression()

        self.vmWriter.writeArithmetic('NOT')
        self.vmWriter.writeIf(L2)

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self._compileStatements()

        self.vmWriter.writeGoto(L1)
        self.vmWriter.writeLabel(L2)

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

        self.vmWriter.writePop('TEMP', 0)

        self.compiledJack.append('/doStatement')

    def _compileReturn(self):
        self.compiledJack.append('returnStatement')

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        if(self.tokens[self.index][1] != ';'):
            self._compileExpression()

        if(self.subroutineType == 'void'):
            self.vmWriter.writePush('CONSTANT', 0)

        self.vmWriter.writeReturn()

        self.compiledJack.append(self.tokens[self.index])
        self.index += 1

        self.compiledJack.append('/returnStatement')

    def _compileExpression(self):
        self.compiledJack.append('expression')

        self._compileTerm()

        commandsToPush = []

        while(self.tokens[self.index][1] == '+' or
              self.tokens[self.index][1] == '-' or
              self.tokens[self.index][1] == '*' or
              self.tokens[self.index][1] == '/' or
              self.tokens[self.index][1] == '&' or
              self.tokens[self.index][1] == '|' or
              self.tokens[self.index][1] == '<' or
              self.tokens[self.index][1] == '>' or
              self.tokens[self.index][1] == '='):
            if(self.tokens[self.index][1] == '-'):
                commandsToPush.append('+')
            commandsToPush.append(self.tokens[self.index][1])

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1
            
            self._compileTerm()

        for command in reversed(commandsToPush):
            self.vmWriter.writeArithmetic(command)

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
           unaryOp = self.tokens[self.index][1]
           
           self.compiledJack.append(self.tokens[self.index])
           self.index += 1

           self._compileTerm()

           self.vmWriter.writeArithmetic(unaryOp)

           self.compiledJack.append('/term')
           return
        #       #        #

        # varName '[' expression ']' #
        elif(self.tokens[self.index + 1][1] == '['):
            
            varName = self.tokens[self.index][1]
            
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            if(self.subroutineST.indexOf(varName) != -1):
                self.vmWriter.writePush(self.subroutineST.kindOf(varName), self.subroutineST.indexOf(varName))
            else:
                self.vmWriter.writePush(self.classST.kindOf(varName), self.classST.indexOf(varName))

            self._compileExpression()

            self.vmWriter.writeArithmetic('ADD')
            self.vmWriter.writePop('POINTER', 1)
            self.vmWriter.writePush('THAT', 0)

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append('/term')
            return
        #            #               #

        # String Constant #
        elif(self.tokens[self.index][0] == 'STRING_CONST'):
            someString = self.tokens[self.index][1]

            self.vmWriter.writePush('CONSTANT', int(len(someString)))
            self.vmWriter.writeCall('String.new', 1)
            self.vmWriter.writePop('TEMP', 0)
            for index, char in enumerate(someString):
                self.vmWriter.writePush('TEMP', 0)
                self.vmWriter.writePush('CONSTANT', ord(char))
                self.vmWriter.writeCall('String.appendChar', 2)
                self.vmWriter.writePop('TEMP', 0)
            self.vmWriter.writePush('TEMP', 0)

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append('/term')
            return
        #       #         #

        elif(self.tokens[self.index + 1][1] == '(' or
             self.tokens[self.index + 1][1] == '.'):
             
             self._compileSubroutineCall()

             self.compiledJack.append('/term')

        else:
            if(self.subroutineST.indexOf(self.tokens[self.index][1]) != -1):
                self.vmWriter.writePush(self.subroutineST.kindOf(self.tokens[self.index][1]),self.subroutineST.indexOf(self.tokens[self.index][1]))
            elif(self.classST.indexOf(self.tokens[self.index][1]) != -1):
                self.vmWriter.writePush(self.classST.kindOf(self.tokens[self.index][1]), self.classST.indexOf(self.tokens[self.index][1]))
            elif(self.tokens[self.index][1] == 'this'):
                self.vmWriter.writePush('POINTER', 0)
            elif(self.tokens[self.index][1] == 'true'):
                self.vmWriter.writePush('CONSTANT', 1)
                self.vmWriter.writeArithmetic('NEG')
            elif(self.tokens[self.index][1] == 'false' or self.tokens[self.index][1] == 'null'):
                self.vmWriter.writePush('CONSTANT', 0)
            else:
                self.vmWriter.writePush('CONSTANT', int(self.tokens[self.index][1]))

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append('/term')

    def _compileSubroutineCall(self):
        # subroutineName '(' expressionList ')' #
        if(self.tokens[self.index + 1][1] == '('):
            subroutineName = self.tokens[self.index][1]

            nVars = 0

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.vmWriter.writePush('POINTER', 0)
            nVars += 1

            nVars =  nVars + self._compileExpressionList()

            self.vmWriter.writeCall(self.className + '.' + subroutineName, nVars)

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            return

        # (className | varName) '.' subroutineName '(' expressionList ')' #
        elif(self.tokens[self.index + 1][1] == '.'):
            classVarName = self.tokens[self.index][1]

            selfRef = 0

            if(self.subroutineST.indexOf(classVarName) != -1):
                self.vmWriter.writePush(self.subroutineST.kindOf(classVarName), self.subroutineST.indexOf(classVarName))
                selfRef = 1
            elif(self.classST.indexOf(classVarName) != -1):
                self.vmWriter.writePush(self.classST.kindOf(classVarName), self.classST.indexOf(classVarName))
                selfRef = 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            subroutineName = self.tokens[self.index][1]

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1            

            nVars = self._compileExpressionList()

            if(self.subroutineST.indexOf(classVarName) != -1):
                className = self.subroutineST.typeOf(classVarName)
            elif(self.classST.indexOf(classVarName) != -1):
                className = self.classST.typeOf(classVarName)
            else:
                className = classVarName

            segment = className + '.' + subroutineName
            self.vmWriter.writeCall(segment, nVars + selfRef)

            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            return

    def _compileExpressionList(self):
        self.compiledJack.append('expressionList')

        nVars = 0

        if(self.tokens[self.index][1] == ')'):
            self.compiledJack.append('/expressionList')
            return nVars

        self._compileExpression()
        nVars += 1

        while(self.tokens[self.index][1] == ','):
            self.compiledJack.append(self.tokens[self.index])
            self.index += 1

            nVars += 1

            self._compileExpression()

        self.compiledJack.append('/expressionList')
        return nVars

    def _nextLabel(self):
        label = self.className + '.L' + str(self.labelIndex)
        self.labelIndex += 1
        return label

    def getCompiledVM(self):
        return self.vmWriter.compiledVM

def singleInArg():

    vmMaker = Analyzer()

    with open(sys.argv[1], 'r') as j:
        vmMaker.sourceJack = j.readlines()

    vmMaker.outputPath = sys.argv[1]
    vmMaker._getJack()
    vmMaker.tokenize()
    vmMaker.compile()
    vmMaker.outputVM()

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

        vmMaker.outputPath = sys.argv[1] + '/' + file
        vmMaker._getJack()
        vmMaker.tokenize()
        vmMaker.compile()
        vmMaker.outputVM()

def run():
    inArg = sys.argv[1]
    if(os.path.isfile(inArg) == True):
        singleInArg()
    else:
        multiInArg()

run()

print("I'm done :)")