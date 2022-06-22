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

        def flattenSource():
            temp = []
            for subList in self.sourceJack:
                for item in subList:
                    temp.append(item)

            self.sourceJack = temp

        def removeEmptyLines():
            self.sourceJack = [item.strip() for item in self.sourceJack]
            self.sourceJack = [item for item in self.sourceJack if item != '']

        def removeInLineComments():
            pass

        def removeBlockComments():
            pass

        def removeEscapedCharacters():
            pass

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

        flattenSource()
        removeEmptyLines()
        removeInLineComments()
        removeBlockComments()
        removeEscapedCharacters()

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
print(len(vmMaker.sourceJack))

print("I'm done :)")