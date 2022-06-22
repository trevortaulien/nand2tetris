print("I'm working :)")

import os
import sys

class Analyzer:

    sourceJack = []

    def __init__(self):
        self.getJack()

    def tokenize(self):
        pass

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

class Tokenizer(Analyzer):

    def __init__(self):
        pass

    def hasMoreTokens(self):
        pass

    def advance(self):
        pass

    def tokenType(self):
        pass

    def keyWord(self):
        pass

    def symbol(self):
        pass

    def identifier(self):
        pass

    def intVal(self):
        pass

    def stringVal(self):
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
vmMaker.tokenize()
vmMaker.compile()
vmMaker.outputVM()

print(vmMaker.sourceJack)


print("I'm done :)")