print("I'm running :)")

import sys
import commandTypes as cmdTyp

class VMTranslator:

    lineIndex = 0
    vmMaster = []       # List of lists with each list at given index containing [commandType, arg1, arg2, rawLine]
    asmLines = []

    def __init__(self):
        with open(sys.argv[1], 'r') as fileIn:
            self.rawVM = fileIn.readlines()

        self.fileInName = sys.argv[0].strip('.py')

    def parse(self):
        self.parser = Parser()
        self.necessaryVM = self.parser.stripUnnecessary(self.rawVM)
        for vmLine in self.necessaryVM:
            subList = [None, None, None, None]
            subList[0] = self.parser.commandType(vmLine)
            
            if(subList[0] == cmdTyp.C_ARITHMETIC):
                subList[1] = vmLine
            elif(subList[0] == cmdTyp.C_RETURN):
                subList[1] = False
            else:
                subList[1] = self.parser.arg1(vmLine)
                
            if((subList[0] == cmdTyp.C_PUSH) or (subList[0] == cmdTyp.C_POP) or (subList[0] == cmdTyp.C_FUNCTION) or (subList[0] == cmdTyp.C_CALL)):
                subList[2] = self.parser.arg2(vmLine)
            else:
                subList[2] = False    
            subList[3] = vmLine            
            self.vmMaster.append(subList)
            self.incrementIndex()

    def codeWrite(self):
        self.writer = CodeWriter()
        for subList in self.vmMaster:
            if(subList[0] == cmdTyp.C_ARITHMETIC):
                asm = self.writer.writeArithmetic(subList)
                self.asmLines.append('// ' + subList[3])
                self._flattenAndAppend(asm,self.asmLines)
                self.asmLines.append('\n')
            elif((subList[0] == cmdTyp.C_PUSH) or (subList[0] == cmdTyp.C_POP)):
                asm = self.writer.writePushPop(subList)
                self.asmLines.append('// ' + subList[3])
                self._flattenAndAppend(asm,self.asmLines)
                self.asmLines.append('\n')

    def outputAsm(self):
        pass

    def hasMoreCommands(self):
        try:
            if (self.rawVM[self.lineIndex]):
                return True
        except:
            return False

    def incrementIndex(self):
        self.lineIndex = self.lineIndex + 1

    def _flattenAndAppend(self, items, appendee):
        for item in items:
            appendee.append(item)

class Parser(VMTranslator):
    
    def __init__(self):
        pass

    def commandType(self, vmLine):
        command = vmLine.split(' ')[0]
        if((command == 'add') or (command == 'sub') or (command == 'neg') or (command == 'eq') or (command == 'gt') or (command == 'lt') or (command == 'and') or (command == 'or') or (command == 'not')):
            return cmdTyp.C_ARITHMETIC
        elif(command == 'pop'):
            return cmdTyp.C_POP
        elif(command == 'push'):
            return cmdTyp.C_PUSH
        else:
            print("ERROR COMMAND TYPE CANNONT BE DETERMNIED!!!")
            print("METHOD: commandType")
            print("vmLine: " + vmLine)
            print("command: " + command)
            quit()

    def arg1(self, vmLine):
        argOne = vmLine.split(' ')[1]
        return argOne

    def arg2(self, vmLine):
        argTwo = vmLine.split(' ')[2]
        return int(argTwo)

    def stripUnnecessary(self, rawVM):
        necessaryVM = self._removeComments(rawVM)
        necessaryVM = self._removeWhitespace(necessaryVM)
        necessaryVM = self._removeInlineComments(necessaryVM)
        necessaryVM = self._removeEOL(necessaryVM)
        return necessaryVM

    def _removeComments(self, lines):
        noCommentsVM = []
        for line in lines:
            if((line[0] == '/') & (line[1] == '/')):
                pass
            else:
                noCommentsVM.append(line)
        return noCommentsVM

    def _removeWhitespace(self, lines):
        noWhitespaceVM = []
        for line in lines:
            if((line == '\n') or (line == '\r') or (line == '\r\n')):
                pass
            else:
                noWhitespaceVM.append(line)
        return noWhitespaceVM

    def _removeInlineComments(self, lines):
        noInlineCommentsVM = []
        for line in lines:
            if(line.find('/') != -1):
                instr_and_comment = line.split('/')
                noInlineCommentsVM.append(instr_and_comment[0])
            else:
                noInlineCommentsVM.append(line)
        return noInlineCommentsVM

    def _removeEOL(self, lines):
        noEOL = []
        for line in lines:
            line = line.replace('\r\n', '')
            noEOL.append(line)

        return noEOL

class CodeWriter(VMTranslator):
    
    def __init__(self):
        pass

    def writeArithmetic(self, subList):
        return 'aX'

    def writePushPop(self, subList):
        segment = subList[1]
        if((segment == 'local') or (segment == 'argument') or (segment == 'this') or (segment == 'that')):
            return self._lattPushPop(subList)
        elif(segment == 'constant'):
            return self._constPush(subList)
        elif(segment == 'static'):
            return self._staticPushPop(subList)
        elif(segment == 'temp'):
            return self._tempPushPop(subList)
        elif(segment == 'pointer'):
            return self._pointPushPop(subList)

    def _lattPushPop(self, subList):
        return 'bX'

    def _constPush(self, subList):
        asm = [
            '@' + str(subList[2]),
            'D=A',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1'
        ]
        return asm

    def _staticPushPop(self, subList):
        variableName = str(sys.argv[1])
        variableName = variableName.strip('.vm')
        variableName = variableName.split('/')
        variableName = variableName[-1]
        variableName = variableName + '.' + str(subList[2])
        if(subList[0] == cmdTyp.C_PUSH):
            asm = [
                '@' + variableName,
                'D=M',
                '@SP',
                'A=M',
                'M=D',
                '@SP',
                'M=M+1'
            ]
        elif(subList[0] == cmdTyp.C_POP):
            asm = [
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                '@' + variableName,
                'M=D'
            ]

        return asm

    def _tempPushPop(self, subList):
        return 'dX'

    def _pointPushPop(self, subList):
        return 'eX'

    def _emptyLine(self):
        return ('')

    def _VMlineAsComment(self,subList):
        return ('//' + subList[3])

translation0 = VMTranslator()
translation0.parse()
print(translation0.vmMaster)
translation0.codeWrite()
print(translation0.asmLines)



print("I'm done :)")